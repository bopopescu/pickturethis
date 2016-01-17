"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import PostForm
from django.http import HttpResponseRedirect
from clarifai.client import ClarifaiApi
import requests
import json
import gensim
import os.path

BASE = os.path.dirname(os.path.abspath(__file__))
word_model = gensim.models.Word2Vec.load_word2vec_format(os.path.join(BASE, 'vectors.bin'),binary=True)
genres = ['abstract', 'accordion', 'afrikaans', 'afrobeat', 'ambient', 'andean', 'anime', 'axe', 'balearic', 'banda', 'bangla', 'barbershop', 'baroque', 'bassline', 'bebop', 'bemani', 'bhangra', 'bluegrass', 'blues', 'bolero', 'boogaloo', 'bounce', 'breakbeat', 'breaks', 'britpop', 'broadway', 'byzantine', 'cabaret', 'cajun', 'calypso', 'cantopop', 'capoeira', 'carnatic', 'ccm', 'cello', 'celtic', 'chanson', 'choral', 'choro', 'christmas', 'clarinet', 'classical', 'comedy', 'comic', 'commons', 'consort', 'corrosion', 'country', 'dancehall', 'demoscene', 'desi', 'didgeridoo', 'disco', 'dixieland', 'downtempo', 'drama', 'drone', 'dub', 'ebm', 'edm', 'electro', 'electronic', 'electronica', 'emo', 'environmental', 'eurovision', 'exotica', 'experimental', 'fado', 'fake', 'filmi', 'flamenco', 'folk', 'footwork', 'freestyle', 'funk', 'gabba', 'galego', 'gamelan', 'glitch', 'gospel', 'grime', 'grindcore', 'grunge', 'guidance', 'hardcore', 'harp', 'hawaiian', 'healing', 'hollywood', 'house', 'idol', 'industrial', 'jazz', 'jerk', 'judaica', 'juggalo', 'jungle', 'klezmer', 'latin', 'lds', 'lilith', 'liturgical', 'lounge', 'lowercase', 'maghreb', 'magyar', 'mallet', 'mambo', 'medieval', 'meditation', 'melancholia', 'merengue', 'metal', 'metalcore', 'minimal', 'mizrahi', 'monastic', 'morna', 'motivation', 'motown', 'neoclassical', 'nepali', 'neurofunk', 'ninja', 'noise', 'nursery', 'oi', 'opera', 'oratory', 'orchestral', 'outsider']

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST)  # Bind data from request.POST into a PostForm
        if form.is_valid():
            imgURL = form.cleaned_data['content']
            app_id = "DbZ4NzfrPL-K_CHHf4y4srnvBUSgMo4Dz9BIbeXt"
            app_secret = "crjTy-8St_kiFkL0wZZCFyrcoWJyOdets8Fa1BNi"
            clarifai_api = ClarifaiApi(app_id,app_secret)
            tags = ''
            embedLink = ''
            try:
                result = clarifai_api.tag_image_urls(imgURL)
            except: #if url is invalid based on clarifai API call
                tags = 'invalid url'
                imgURL = ''
            if tags!='invalid url':
                tagList = result['results'][0]['result']['tag']['classes']
                bestGenre = imgscore(tagList,genres)
                r = requests.get('https://api.spotify.com/v1/search?q=%22'+bestGenre+'%22&type=playlist')
                jsonStuff = r.json()
                uri = jsonStuff['playlists']['items'][0]['uri']
                embedLink = "https://embed.spotify.com/?uri="+uri
            return render(
                request,
                'app/index.html',
                {
                    'form': form,
                    'imgsrc': imgURL,
                    'debugText': tags,
                    'playlistURI': embedLink,
                    'year':datetime.now().year,
                }
            )
    return render(
        request,
        'app/index.html',
        {
            'form': form,
            'imgsrc': '',
            'debugText': '',
            'playlistURI': '',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )


def imgscore(words,genres):
    l = 0.0
    summ = []
    for genre in genres:
        for word in words:
            try:
                simScore = word_model.similarity(genre,word)
                l += simScore
            except:
                 pass
        summ.append(l)
        l = 0
    return(genres[summ.index(max(summ))])
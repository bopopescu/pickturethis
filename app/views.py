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

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST)  # Bind data from request.POST into a PostForm
        if form.is_valid():
            content = form.cleaned_data['content']
            app_id = "DbZ4NzfrPL-K_CHHf4y4srnvBUSgMo4Dz9BIbeXt"
            app_secret = "crjTy-8St_kiFkL0wZZCFyrcoWJyOdets8Fa1BNi"
            clarifai_api = ClarifaiApi(app_id,app_secret)
            tags = ''
            try:
                result = clarifai_api.tag_image_urls(content)
            except:
                tags = 'invalid url'
                content = ''
            if tags!='invalid url':
                tagList = result['results'][0]['result']['tag']['classes']
                for tag in tagList:
                    tags += tag + ' '
            r = requests.get('https://api.spotify.com/v1/search?q=%22afrobeat%22&type=playlist')
            jsonStuff = r.json()
            #playlistInfo = json.loads(jsonFile)
            tags = jsonStuff['playlists']['items'][0]['uri']
            return render(
                request,
                'app/index.html',
                {
                    'form': form,
                    'test': content,
                    'tags': tags,
                }
            )
    return render(
        request,
        'app/index.html',
        {
            'form': form,
            'test': '',
            'tags': '',
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

import gensim

#word_model = gensim.models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

#filtered_genres = ['abstract', 'accordion', 'afrobeat', 'ambient', 'anime', 'bachata', 'banda', 'bangla', 'barbershop', 'baroque', 'bassline', 'beatdown', 'bebop', 'benga', 'bhangra', 'bluegrass', 'blues', 'bolero', 'boogaloo', 'bounce', 'breakbeat', 'breakcore', 'breaks', 'broadway', 'byzantine', 'cabaret', 'cajun', 'calypso', 'capoeira', 'carnatic', 'ccm', 'ceilidh', 'cello', 'celtic', 'chanson', 'chillwave', 'chiptune', 'choral', 'choro', 'christmas', 'clarinet', 'classical', 'comedy', 'comic', 'commons', 'consort', 'corrosion', 'country', 'cowpunk', 'crunk', 'cumbia', 'dancehall', 'dangdut', 'desi', 'didgeridoo', 'disco', 'dixieland', 'doujin', 'downtempo', 'drama', 'drone', 'dub', 'dubstep', 'duranguense', 'ebm', 'electro', 'electroclash', 'electronic', 'electronica', 'emo', 'enka', 'environmental', 'eurovision', 'exotica', 'experimental', 'fado', 'fake', 'filmi', 'fingerstyle', 'flamenco', 'folk', 'footwork', 'forro', 'freestyle', 'funk', 'gabba', 'gamelan', 'glitch', 'gospel', 'grime', 'grindcore', 'grunge', 'guidance', 'hardcore', 'hardstyle', 'harp', 'hawaiian', 'healing', 'highlife', 'hiplife', 'hollywood', 'horrorcore', 'house', 'hyphy', 'idol', 'industrial', 'jazz', 'jerk', 'juggalo', 'jungle', 'kirtan', 'klezmer', 'kompa', 'kuduro', 'kwaito', 'latin', 'lds', 'liturgical', 'lounge', 'lowercase', 'mallet', 'mambo', 'mariachi', 'mashup', 'mathcore', 'mbalax', 'medieval', 'meditation', 'melancholia', 'merengue', 'metal', 'metalcore', 'microhouse', 'minimal', 'monastic', 'morna', 'motivation', 'motown', 'nasheed', 'neoclassical', 'nepali', 'nerdcore', 'ninja', 'noise', 'norteno', 'nursery', 'oi', 'opera', 'opm', 'oratory', 'orchestral', 'outsider']

def imgscore(words,genres):
    l = []
    summ = []
    for genre in genres:
        for word in words:
            l.append(word_model.similarity(genre,word))
        summ.append(sum(l))
        l = []
    return(genres[summ.index(max(summ))])


#words = ['hello','cat']  #comes from image

#print(imgscore(words,filtered_genres))

from datetime import datetime
from urllib import request
from django.shortcuts import render
from django.http import HttpRequest
import joblib

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,'app/index.html',{'title':'Home Page','year':datetime.now().year,})

def result(request):

    pipe = joblib.load('saved_IMDB_pipe.sav')
    title = request.GET['Title']
    title = title.title()

    text = request.GET['Review']

    ans = pipe(text)
    if ans[0]['label'] == 'LABEL_1':
        rating = int(ans[0]['score'] * 10) + 1
        sentiment = 'POSITIVE'
    else:
        rating = rating = int(11 - (ans[0]['score'] * 10))
        sentiment = 'NEGATIVE'
    
    return render(
        request,'app/result.html', {'sentiment':sentiment, 'rating':rating, 'title': title, 'text': text})

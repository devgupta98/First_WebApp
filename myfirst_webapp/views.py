import operator

from django.http import HttpResponse
from django.shortcuts import render
from . import counter


def home(request):
    return render(request, 'index.html',{'key1': 'I am coming from python code'})


def results(request):
    article = request.GET['article']
    var_dict, word_count = counter.count(article)
    return render(request, 'results.html', {'article': article, 'word_count': word_count, 'dict_words': var_dict})



def downloads(request):
    return HttpResponse('<h1>This is downloads <h1/>')
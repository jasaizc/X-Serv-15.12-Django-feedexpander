from django.shortcuts import render
from models import Usuarios
import feedparser
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def tweet(request, username):
    url = "https://twitrss.me/twitter_user_to_rss/?user=" + username
    parseo = feedparser.parse(url);
    salida = ""
    for number in range(5):
        salida += parseo.entries[number].title + "<br>"
    return HttpResponse(str(salida))
    
def NotFound(request,recurso):  
  valor = "Valor No encontrado, quiere crear uno, o visualizarlo, pruebe con <a href='/usuarios'>/usuarios</a>: " + logueo(request)
  return HttpResponse(valor)

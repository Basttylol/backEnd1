from django.shortcuts import render
from django.http import HttpResponse
import datetime 
# Create your views here.

def hola(request):
    saludo = "<h1>HOLA MUNDO!!!!!</h1>"
    return HttpResponse(saludo)

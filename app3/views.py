from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def saludo2(requests):
    return HttpResponse("<h1>Hola</h1>")
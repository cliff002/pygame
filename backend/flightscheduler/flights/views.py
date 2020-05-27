from django.shortcuts import render
from django.http import HTTpResponse 

# Create your views here.

def index(request):
    return HTTpResponse("<h1>Hello, Flight Scheduler!</h1>")
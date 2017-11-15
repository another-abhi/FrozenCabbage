from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Patient Login")
# Create your views here.

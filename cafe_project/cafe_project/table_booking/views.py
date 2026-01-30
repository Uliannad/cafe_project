from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Привіт, мій преший view!")
# Create your views here.

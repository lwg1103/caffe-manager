from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<html><head><title>Caffe Manager</title></head><body>home</body></html>")

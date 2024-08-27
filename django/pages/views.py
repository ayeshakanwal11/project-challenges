from django.shortcuts import render


from django.shortcuts import render


from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse("Hello, World!")
# pages/views.py
from django.shortcuts import render

# Create your views here.
# pages/views.py
from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse("Hello, World!")
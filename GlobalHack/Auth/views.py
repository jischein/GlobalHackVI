from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {'login':login}
    return render(request, '/registration/base.html', context)

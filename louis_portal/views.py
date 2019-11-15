from django.shortcuts import render
from django.http import request

# Create your views here.

def master(request):
    return render(request, 'master.html')
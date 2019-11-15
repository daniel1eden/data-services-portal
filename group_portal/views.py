from django.shortcuts import render
from django.http import request

def master_home(request):
    return render(request, 'master_home.html')
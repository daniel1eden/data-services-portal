from django.shortcuts import render
from django.http import request

# Create your views here.

def index(request):
    return render(request, 'index.html')


def dp(request):
    return render(request, 'dp.html')


def ethics(request):
    return render(request, 'ethics.html')


def team(request):
    return render(request, 'team.html')


def faq(request):
    return render(request, 'FAQ.html')


def prog(request):
    return render(request, 'prog.html')


def trans(request):
    return render(request, 'trans.html')
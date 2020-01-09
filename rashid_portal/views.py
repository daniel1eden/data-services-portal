from django.shortcuts import render
from django.http import request

# Create your views here.
def rashid_index(request):
    return render(request, 'rashid_index.html')
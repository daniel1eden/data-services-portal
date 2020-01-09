from django.shortcuts import render
from django.http import request

# Create your views here.

def home(request):
    return render(request, 'home_page.html')
    

def change_log(request):
    return render(request, 'changes_log_page.html')


def faq(request):
    return render(request, 'faqs_page.html')


def help_desk(request):
    return render(request, 'helpdesk_page.html')


def team(request):
    return render(request, 'team_page.html')


def timeline(request):
    return render(request, 'timeline_page.html')


def hints_tips(request):
    return render(request, 'hints_tips.html')


def enhance_questions(request):
    return render(request, 'enhance_questions.html')


def question_structure(request):
    return render(request, 'question_structure.html')


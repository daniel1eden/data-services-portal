from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('changes-log/', views.change_log, name='changes_log'),
    path('FAQ/', views.faq, name='faqs'),
    path('help-desk/', views.help_desk, name='help_desk'),
    path('team/', views.team, name='meet_the_team'),
    path('timeline/', views.timeline, name='timeline'),
]

from django.urls import path
from . import views

urlpatterns = [
   path('', views.rashid_index, name='rashid_index') 
]

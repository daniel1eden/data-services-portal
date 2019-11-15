from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data-processing/', views.dp, name='dp'),
    path('ethics/', views.ethics, name='ethics'),
    path('FAQ/', views.faq, name='faq'),
    path('prog/', views.prog, name='prog'),
    path('team/', views.team, name='team'),
    path('translation/', views.trans, name='translation'),
]






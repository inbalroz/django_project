from django.urls import path
from . import views

urlpatterns = [path('', views.home, name='blog-home'),
    path('', views.home, name='blog-home'),
    path('Ainstructions/', views.instructions, name='blog-instructions'),
    path('Binstructions/', views.instructions, name='blog-Binstructions'),
    path('blank/', views.blank, name='blog-blank'),
]

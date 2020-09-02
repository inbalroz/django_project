from django.urls import path
from . import views

urlpatterns = [path('', views.home, name='blog-home'),
    path('', views.home, name='blog-home2'),
    path('Ainstructions/', views.instructions, name='blog-instructions'),
    path('Ainstructionsbefore/', views.instructionsbefore, name='blog-instructionsbefore'),
    path('Binstructions/', views.instructions, name='blog-Binstructions'),
    path('Binstructionsbefore/', views.instructionsbefore, name='blog-Binstructionsbefore'),
    path('blank/', views.blank, name='blog-blank'),
    path('completed/', views.completed, name='blog-completed'),
    path('exam/', views.exam, name='blog-exam'),
    path('examB/', views.examB, name='blog-examB'),
]

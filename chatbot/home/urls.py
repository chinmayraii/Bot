from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.chat),
    path('chatapi',views.chatapi)    
]
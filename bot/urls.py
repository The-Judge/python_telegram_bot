from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.index),
    path('hook/', views.talkin_to_me_bruh),
]

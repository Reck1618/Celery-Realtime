from django.urls import path
from . import views

urlpatterns = [
    path('chat_app/', views.index, name='index'),
]
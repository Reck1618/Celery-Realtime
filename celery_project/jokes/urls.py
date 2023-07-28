from django.urls import path
from . import views

urlpatterns = [
    path('jokes/', views.index, name='index')
]
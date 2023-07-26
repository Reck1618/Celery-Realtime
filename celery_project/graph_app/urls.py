from django.urls import path
from . import views

urlpatterns = [
    path('graph_app/', views.index, name='index'),
]
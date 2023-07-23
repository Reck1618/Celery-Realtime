from django.urls import path
from . import views

urlpatterns = [
    path('integers_app/', views.index, name='index'),
]
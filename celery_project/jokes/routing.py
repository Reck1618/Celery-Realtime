from django.urls import path
from . import consumers

jokes_urlpatterns = [
    path('ws/jokes/', consumers.JokeConsumer.as_asgi()),
]
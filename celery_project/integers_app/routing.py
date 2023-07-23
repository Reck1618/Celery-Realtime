from django.urls import path
from . import consumers

ws_urlpatterns = [
    path('ws/integers/', consumers.IntegerConsumer.as_asgi()),
]


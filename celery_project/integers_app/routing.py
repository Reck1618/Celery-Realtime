from django.urls import path
from . import consumers

integers_urlpatterns = [
    path('ws/integers/', consumers.IntegerConsumer.as_asgi()),
]


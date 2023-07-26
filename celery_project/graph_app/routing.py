from django.urls import path
from . import consumers

graph_urlpatterns = [
    path('ws/graph/', consumers.GraphConsumer.as_asgi()),
]
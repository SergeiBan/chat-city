from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    re_path("(?P<spot_name>\w+)", consumers.ChatConsumer.as_asgi()),
]

from django.contrib import admin
from django.urls import path, include
from spots import consumers

websocket_urlpatterns = [
    path(r'ws/', consumers.SpotConsumer.as_asgi()),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api'))
]

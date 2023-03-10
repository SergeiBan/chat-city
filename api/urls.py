from django.urls import path, include
from rest_framework.routers import DefaultRouter
from spots.views import SpotViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'spots', SpotViewSet, basename='spot')

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.authtoken')),
    path('v1/', include(router.urls))
]

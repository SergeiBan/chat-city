from django.shortcuts import render
from rest_framework import viewsets
from spots.models import Spot
from spots.serializers import SpotSerializer


class SpotViewSet(viewsets.ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer

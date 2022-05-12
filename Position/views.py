from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SoccerSerializer
from .models import Soccer

class SoccerView(viewsets.ModelViewSet):
    serializer_class = SoccerSerializer
    queryset = Soccer.objects.all()
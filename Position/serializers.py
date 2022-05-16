from rest_framework import serializers
from .models import Soccer

class SoccerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soccer
        fields = '__all__'
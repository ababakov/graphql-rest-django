from rest_framework import serializers
from .models import Actor, Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = []


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        exclude = []


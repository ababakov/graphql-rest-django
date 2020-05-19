from django.shortcuts import render
from rest_framework import viewsets
from movies.serializers import MovieSerializer, ActorSerializer
from movies.models import Movie, Actor

class ActorsViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


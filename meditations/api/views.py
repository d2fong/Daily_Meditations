from rest_framework import generics
from ..models import Author, Meditation
from .serializers import AuthorSerializer, MeditationSerializer

class AuthorListView(generics.ListAPIView):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveAPIView):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer


class MeditationListView(generics.ListAPIView):
	queryset = Meditation.objects.all()
	serializer_class = MeditationSerializer


class MeditationDetailView(generics.ListAPIView):
	queryset = Meditation.objects.all()
	serializer_class = MeditationSerializer
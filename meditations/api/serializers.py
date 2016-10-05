from rest_framework import serializers
from ..models import Author, Meditation


class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = ('id', 'first_name', 'last_name')


class MeditationSerializer(serializers.ModelSerializer):
	author = AuthorSerializer()

	class Meta:
		model = Meditation
		fields = ('id', 'author', 'category', 'content')
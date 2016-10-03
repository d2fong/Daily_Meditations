from rest_framework import serializers
from ..models import Author


class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = ('id', 'first_name', 'last_name')

class MeditationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Meditation
		fields = ('id', 'author', 'category', 'content')
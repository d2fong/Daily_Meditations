from django.db import models
from django.utils import timezone

# Create your models here.


class Meditation(models.Model):
	CATEGORY = (
		('stoicism', 'stoicism'),
	)

	author = models.ForeignKey('Author')
	category = models.CharField(max_length=40, choices=CATEGORY)
	content = models.TextField()
	created_date = models.DateTimeField(
		default = timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)


class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)


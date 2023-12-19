from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	name = models.CharField(max_length=200, null=True)
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=100)
	bio = models.TextField(max_length=250, null=True)
	avatar = models.ImageField(null=True)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["username"]

	def __str__(self):
		return self.username




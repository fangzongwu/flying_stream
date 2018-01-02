from django.db import models

# Create your models here.
class UserModel(models.Model):
	nick_name = models.CharField(max_length=50)
	email = models.EmailField(blank=True)
	password = models.CharField(max_length=20)

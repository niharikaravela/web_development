from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=50)
	rno = models.CharField(max_length=20)
	email = models.EmailField()
	mobile = models.CharField(max_length=10)
	age = models.IntegerField()

	def __str__(self):
		return self.name
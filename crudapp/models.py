from django.db import models

# Create your models here.
class Student(models.Model):
	genders = [('Female','Female'),('Male','Male'),('Others','Others')]
	fname = models.CharField(max_length=30)
	lname = models.CharField(max_length=20)
	uname = models.CharField(max_length=50)
	rno = models.CharField(max_length=20)
	email = models.EmailField(max_length=30)
	mobile = models.CharField(max_length=10)
	gender = models.CharField(max_length=15,choices=genders)
	age = models.IntegerField(null=True)

	def __str__(self):
		return self.uname + ' ' + self.email
from django import forms
from django.forms import ModelForm
from formsapp.models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		#fields = ['name','email']
		fields = '__all__'	
		
from django.urls import path
from formsapp import views

urlpatterns= [
	path('d/',views.d,name='d'),
	path('reg/',views.reg,name='reg'),

]
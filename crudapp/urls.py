from django.urls import path
from crudapp import views
urlpatterns = [
	path('demo1/',views.demo),
	path('registration/',views.register,name='register'),
	path('details/',views.details,name='details'),
	path('update/<int:id>',views.update,name='update'),
	path('delete/<int:id>',views.delete,name='delete'),
	path('contact/',views.contact,name='contact'),
	path('main/',views.home,name='home'),
	path('signin/',views.signin,name='signin'),

]
"""vitw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from vitapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/',views.display),
    path('home/',views.info),
    path('task/',views.bull),
    path('variable/<str:name>/',views.stringvalue),
    path('age/<int:age>/',views.agenum),
    path('age1/<int:age>/',views.agenum1),
    path('both/<str:name>/<int:num>/',views.total),
    path('samplehtml/',views.samplehtmlex,name='sample'),
    path('demo/',views.htmlexcss,name='call'),
    path('solid/',views.external,name=''),
    path('boot/',views.bootstrapex,name=''),
    path('login/',views.loginpage,name=''),
    path('register/',views.registration,name=''),
    path('',include('crudapp.urls')),
    path('forms/',include('formsapp.urls')),
]

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
	return HttpResponse("<center><h1>Welcome to Django session</h1></center>")

def info(request):
	return HttpResponse("<h3>Create a Project.Whether you are on Windows or linux </h3><br><p>there are three steps in creating a project. <br>Step-1:create a app using the comand.<br>  Step-2: this includes creating an app using the manage controller.<br>Step-3:register your app. </p>")

def bull(request):
	return HttpResponse("<center><h1><b><i>Django</i></b></h1></center><br><h2>This is Niharika.</h2><br><br><h3>This is the Description.<p>Django is a Python-based free and open-source web framework that follows the model-template-views architectural pattern. It is maintained by the Django Software Foundation, an American independent organization established as a 501 non-profit</p></h3><br><h5>Organised by APPSDC in VITW</h5>")

def stringvalue(request,name):
	return HttpResponse("Hello......"+name)

def agenum(request,age):
	return HttpResponse("Age : "+str(age))

def agenum1(request,age):
	return HttpResponse("Age : %d "%age)

def total(request,name,num):
	return HttpResponse("Hello.... : "+name+" <t>  Age .. : "+str(num))

def samplehtmlex(request):
	return render(request,'vitapp/sample.html')

def htmlexcss(request):
	return render(request,'vitapp/demo.html')

def external(request):
	return render(request,'vitapp/extern.html')

def bootstrapex(request):
	return render(request,'vitapp/bootstrapex.html')

def loginpage(request):
	return render(request,'vitapp/login.html')

def registration(request):
	if request.method == 'POST':
		Fname = request.POST.get('fname')
		Lname = request.POST.get('lname')
		Uname = request.POST.get('uname')
		RollNo = request.POST.get('rollno')
		Password = request.POST.get('password')
		Email = request.POST.get('email')
		Mobile = request.POST.get('mobilenumber')
		#print(Fname,Lname,Uname,RollNo,Email,Mobile)
		return render(request,'vitapp/details.html',{'Fname':Fname,'Lname':Lname,'Uname':Uname,'RollNo':RollNo,'Email':Email,'Mobile':Mobile})
	return render(request,'vitapp/registration.html')
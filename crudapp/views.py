from django.shortcuts import render,redirect
from django.http import HttpResponse
from crudapp.models import Student

# Create your views here.
def demo(request):
	return HttpResponse("Hello World!!!")

def register(request):
	if  request.method == 'POST':
		fn=request.POST.get('fname')
		ln=request.POST.get('lname')
		un=request.POST.get('uname')
		em=request.POST.get('email')
		rn=request.POST.get('rno')
		ph=request.POST.get('mobile')
		gen=request.POST.get('gender')
		a=request.POST.get('age')
		Student.objects.create(fname=fn,lname=ln,uname=un,email=em,rno=rn,mobile=ph,gender=gen,age=a)
		return redirect('details')
	return render(request,'register.html')


def details(request):
	info = Student.objects.all()
	context = {'info':info}
	return render(request,'details.html',context)

def update(request,id):
	data = Student.objects.get(id=id)
	if request.method == 'POST':
		data.fname = request.POST['fname']
		data.lname = request.POST['lname']
		data.uname = request.POST['uname']
		data.rno = request.POST['rno']
		data.email = request.POST['email']
		data.mobile = request.POST['mobile']
		data.gender = request.POST['gender']
		data.age = request.POST['age']
		data.save()
		return redirect('details')
	return render(request,'update.html',{'data':data})

def contact(request):
	return render(request,'contact.html')

def delete(request,id):
	obj=Student.objects.get(id=id)
	if request.method == 'POST':
		obj.delete()
		return redirect('details')
	return render(request,'delete.html',{'obj':obj})

def home(request):
	return render(request,'home.html')

def signin(request):
	return render(request,'signin.html')
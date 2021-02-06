from django.shortcuts import render
from django.http import HttpResponse
from formsapp.forms import StudentForm

# Create your views here.
def d(request):
	return HttpResponse("Hello!!")

def reg(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		form.save()
	form = StudentForm()
	return render(request,'forms/reg.html',{'form':form})
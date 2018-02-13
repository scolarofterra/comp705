from django.shortcuts import render
from .models import Education,Experiance
# Create your views here.
def exper(request):

	ex = Experiance.objects
	context = {"experiance":ex}
	return render(request,'~/templates/resume',context)


def exper(request):

	ex = Experiance.objects
	context = {"experiance":ex}
	return render(request,'~/templates/resume',context)
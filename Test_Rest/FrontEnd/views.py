from django.shortcuts import render
import datetime
# Create your views here.

def Dashboard(request):
    return render(request,'index.html')


def Add_Form_Data(request):
	djangodate = datetime.datetime.now()
	return render(request,'form_data.html',{'djangodate':djangodate})

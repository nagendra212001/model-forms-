from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
from app.forms import *

def insert_topic(request):
    form=topicForm()
    d={'form':form}
    if request.method=="POST":
        form_data=topicForm(request.POST)
        form_data.save()
        return HttpResponse("topic models inserted succesfiilly by modelforms")
    return render(request,"insert_topic.html",d)


def insert_webpage(request):
    form=webpageForm()
    d={'form':form}
    if request.method=="POST":
        form_data=webpageForm(request.POST)
        form_data.save()
        return HttpResponse("webpage models inserted succesfiilly by modelforms")
    return render(request,"insert_webpage.html",d)



def insert_acessrecord(request):
    form=access_recordForm()
    d={'form':form}
    if request.method=="POST":
        form_data=access_recordForm(request.POST)
        form_data.save()
        return HttpResponse("accessrecord models inserted succesfiilly by modelforms")
    return render(request,"insert_acessrecord.html",d)



def displaywebpage(request):
    k=webpage.objects.all()
    d={'k':k}
    return render(request,"displaywebpage.html",d)
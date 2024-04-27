from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable" : "this is sent"
    }
    return render(request,'index.html',context)
    return render(request, 'index.html',context)
   # return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html',)

    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html',)

    #return HttpResponse("this is services page")


def contact(request):
    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = contact(name=name,email=email,message=message)
        contact.save()
        messages.success(request, "your message has been sent!")

    return render(request, 'contact.html',)
    #return HttpResponse("this is contact page")


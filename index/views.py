from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from .models import User
from .forms import UserForm
# Create your views here.

def userView(request):
    if request.method == "POST":
        form=UserForm(request.POST)
        if form.is_valid() and request.POST.get("signupbtn"):
            form.save()
            return redirect("home")
        elif form.is_valid() and request.POST.get("loginbtn"):
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = User.objects.get(username=username,password=password)
            if user is not None:
                return HttpResponseRedirect("/home")
            else:
                return HttpResponse("Invalid"+username+" "+password)

    else:
        form=UserForm()
    return render(request,"index/index.html",{"form":form})

def home(request):
    return render(request,"index/home.html")

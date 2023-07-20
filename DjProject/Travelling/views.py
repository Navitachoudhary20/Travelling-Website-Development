from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render,redirect
from Travelling.forms import AuthenticationForm
from Travelling.models import Authentication

def Auth(request):
    if request.method == "POST":
        form=AuthenticationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/successful')
            except:
                pass
    else:
        form = AuthenticationForm()
    return render(request,'href.html',{'form':form})

def successful(request):
      return render(request,'successful.html')
def index(request):
    return render(request,"href.html")
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact_us(request):
      return render(request,'contact_us.html') 
def login_or_signup(request):
  return render(request,'login_or_Signup.html') 
# def travelling(request):
#     return render(request,'home.html')

# from django.shortcuts import render, redirect 
# # from registrationapp.forms import MemberForm 
# # from registrationapp.models import Member

# from Travelling.forms import UserForm 
# from Travelling.models import User

# from django.http import HttpResponse
# from django.template import loader

# # Create your views here. 
# def register(request): 
#    if request.method == "POST": 
#       form = UserForm(request.POST) 
#       if form.is_valid(): 
#          try: 
#             form.save() 
#             return redirect('/success') 
#          except: 
#             pass 
#    else: 
#       form = UserForm() 
#    return render(request,'register.html',{'form':form}) 

# def success(request): 
#    return render(request,"success.html")

  

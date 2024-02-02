from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from books.models import Books
from books.forms import BookModelForm,RegistrationForm

# Create your views here.

class SignUpView(View):
    def get (self,request,*args, **kwargs):
        form=RegistrationForm()
        return render(request,"sign_up.html",{"form":form})
    def post (self,request,*args, **kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            print("Created")
            return redirect("sign-in")
        else:
            print("invalid")
            return render(request,"sign_up.html",{"form":form})

class UserBookListView(View):
    def get (self,request,*args, **kwargs):
        qs=Books.objects.all()
        return render (request,"user_home.html",{"books":qs})
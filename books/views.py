from django.shortcuts import render,redirect
from django.views.generic import View,ListView
from books.forms import BookModelForm
from books.models import Books
from django.contrib.auth.models import User 
from books.forms import RegistrationForm,LogInForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.


    
class SignInView(View):
    def get (self,request,*args, **kwargs):
        form=LogInForm()
        return render (request,"sign_in.html",{"form":form})
    def post(self,request,*args, **kwargs):
        form=LogInForm(request.POST)
        if form.is_valid():
            print("Valid")
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                print("login")
                login(request,user_object)
                if request.user.is_superuser:
                    return redirect ('home')
                else:
                    return redirect ("user-bk-home")
            else:
                print("invalid")
                return render (request,"sign_in.html",{"form":form})
            
class LogOutView(View):
    def get (self,request,*args, **kwargs):
        logout(request)
        return redirect ('sign-in')

class IndexView(ListView):
    model=Books
    template_name="booklist.html"
    context_object_name="books"
    
    def post(self, request, *args, **kwargs):
        data = request.POST.get("book")

        form_name = Books.objects.filter(name__icontains=data)
        form_genres = Books.objects.filter(genres__icontains=data)

        form = form_name.union(form_genres)

        return render(request, "booklist.html", {"books": form})
        

class BookCreateView(View):
    def get(self,request,*args, **kwargs):
        form=BookModelForm()
        return render (request,"bookadd.html",{"form":form})
    def post(self,request,*args, **kwargs):
        form=BookModelForm(request.POST,files=request.FILES)
        flag=False
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            flag=True
            return redirect ('home')
        else:
            flag=False
            print("invalid")
            return render (request,"bookadd.html",{"flag":flag})
    

    
class BookDetailView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Books.objects.get(id=id)
        return render (request,"bookdetail.html",{"data":qs})
    
class BookUpdateView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        bk_obj=Books.objects.get(id=id)
        form=BookModelForm(instance=bk_obj)
        return render (request,"bkupdate.html",{"data":form})
        
    def post (self,request,*args, **kwargs):
        id=kwargs.get("pk")
        bk_obj=Books.objects.get(id=id)
        form=BookModelForm(request.POST,request.FILES,instance=bk_obj)
        if form.is_valid():
            form.save()
            return redirect ('bk-view',kwargs.get("pk"))
        else:
            return render (request,"bkupdate.html",{"data":form})
        
class BookDeleteView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        Books.objects.get(id=id).delete()
        return redirect('home')
        
       

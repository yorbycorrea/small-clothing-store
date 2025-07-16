from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import  SignUpForm
from django import forms


def category_page(request):
    # Puedes agregar aquí la lógica que necesites para obtener datos de la categoría si es necesario
    # Por ahora, simplemente renderizamos la página sin datos específicos
    return render(request, 'category.html')


def category(request, foo):
    #reemplazamos los espacios por signos
    foo = foo.replace('-','')
    
    try:
        #Buscamos la categoria
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html' ,{'products':products, 'category':category})
        
    except:
        messages.success(request, ("La Categoria no Existe..."))
        return redirect('home')    


def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Ha inicidado sesion correctamente"))
            return redirect('home')
        else:
            messages.success(request, ("Error al iniciar sesion "))
            return redirect('login')
    
    else:
        return render(request, 'login.html', {})   
        
        
    

def logout_user(request):
    logout(request)
    messages.success(request,("Gracias por pasar por nuestra tienda"))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("Te has registrado Correctamente, Por favor inicia Sesion"))
            return redirect('home')
        else:
            messages.success(request,("Uppss!! Hubo un problema al registrate, por favor intetalo mas tarde"))
            return redirect('register')
            
    return render(request, 'register.html', {'form':form})
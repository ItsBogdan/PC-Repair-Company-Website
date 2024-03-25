from django.shortcuts import render, redirect
from .models import Order
from .forms import RegisterForm, LoginForm, OrderForm
from django.contrib.auth import login, authenticate

def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render (request, 'my_orders.html', {'orders': orders})

def homepage(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
        return render(request, 'register.html', {'form': form})

def log_in(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('homepage')
        return render(request, 'login.html', {'form': form})

def create_order(request):
    if request.method == "GET":
        form = OrderForm()
        return render(request, 'create_order.html', {'form': form})
    elif request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('my_orders')
        return render(request, 'create_order.html', {'form': form})
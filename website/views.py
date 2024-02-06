from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record


def home(request):
    records = Record.objects.all()
    return render(request, 'home.html', {'records':records})

def login_user(request):

    

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You've have been logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in")
            return redirect('login')

    else:
        return render(request, 'loginusr.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,"You've have been logged out")
    return redirect('home')

def register_user(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,"You've have been successfully registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'regusr.html', {'form':form})
    
    return render(request, 'regusr.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})

from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import login,authenticate

def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'users/login.html',{'form':form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                messages.success(request,f'Hi {username.title()},,welcome back!')
                return redirect('posts')
        
    messages.error(request,f'Invalid Username or Password')
    return render(request,'users/login.html',{'form':form})
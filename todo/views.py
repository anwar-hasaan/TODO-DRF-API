from django.shortcuts import render, redirect
from todo.forms import UserRegiterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from todo.models import User

@login_required(login_url='/login')
def home(request):
    email = request.user.email
    
    token = User.objects.filter(uid='16551f46-35d0-4fb9-ad20-39cfbd66f988').first().is_admin

    return render(request, 'base.html' ,{'uid': token})

def register(request):
    if request.method == 'POST':
        form = UserRegiterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successful')
            return redirect('todo:login')
        messages.error(request, form.errors)
    else:
        form = UserRegiterForm()
    context = {'form': form}
    return render(request, 'auth/registration.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Login Success')
                return redirect('/')
            else:
                messages.error(request, 'Email or password is invalid')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'auth/login_form.html', context)

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout Success')
    return redirect('/login')
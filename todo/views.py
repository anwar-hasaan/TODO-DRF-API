from django.shortcuts import render, redirect
from todo.forms import UserRegiterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from todo.models import User, Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todo.serializers import TodoSerializer

@api_view(['POST'])
def get_all_task(request):
    dev_uid = request.data['dev_uid']
    user_id = request.data['user_id']

    dev = User.objects.get(uid=dev_uid)
    
    all_task = Todo.objects.filter(dev_ref=dev, user_id=user_id)
    serializer = TodoSerializer(all_task, many=True)

    return Response({'status': 200, 'data': serializer.data, 'message': 'all data'})   

@login_required(login_url='/login')
def home(request):
    return render(request, 'base.html' ,)

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
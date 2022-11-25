from django.shortcuts import render, redirect
from todo.forms import UserRegiterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from todo.models import User, Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todo.serializers import TodoSerializer
from rest_framework import status

@api_view(['GET'])
def welcome(request):
    return Response({'message': 'Welcome to this todo-api'})

@api_view(['POST'])
def get_all_task(request):
    try:
        dev_uid = request.data['dev_uid']
        user_id = request.data['user_id']
        dev = User.objects.get(uid=dev_uid)
        all_task = Todo.objects.filter(dev_ref=dev, user_id=user_id)
        if all_task.first() is not None:
            serializer = TodoSerializer(all_task, many=True)
            # this is returing all task if credentials is ok
            return Response({'message': 'your all tasks', 'tasks': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': 'No task available or invalid user'}, status=status.HTTP_404_NOT_FOUND)        
    except Exception as error:
        error = str(error)
        if 'dev_uid' in error or 'user_id' in error:
            error = error + ' not provided'
        return Response({'errors': error}, status=status.HTTP_400_BAD_REQUEST)   

@api_view(['POST'])
def task_details(request):
    try:
        dev_uid = request.data['dev_uid']
        user_id = request.data['user_id']
        task_uid = request.data['task_uid']
        dev = User.objects.get(uid=dev_uid)
        task = Todo.objects.filter(dev_ref=dev, user_id=user_id, uid=task_uid).first()
        if task:
            serializer = TodoSerializer(task)
            # this is returing all task if credentials is ok
            return Response({'message': 'your tasks details', 'task': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': 'No task available or invalid user'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as error:
        error = str(error)
        if 'dev_uid' in error or 'user_id' in error or 'task_uid' in error:
            error = error + ' not provided'
        return Response({'errors2': error}, status=status.HTTP_400_BAD_REQUEST) 

@login_required(login_url='/login')
def home(request):
    return render(request, 'auth/home.html')

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
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login Success')
            return redirect('/')
        else:
            messages.error(request, 'Email or password is invalid')
    return render(request, 'auth/login_form.html')
    # login with Django form
    # if request.method == 'POST':
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         email = form.cleaned_data.get('email')
    #         password = form.cleaned_data.get('password')
    #         user = authenticate(request, username=email, password=password)
    #         if user:
    #             login(request, user)
    #             messages.success(request, 'Login Success')
    #             return redirect('/')
    #         else:
    #             messages.error(request, 'Email or password is invalid')
    # else:
    #     form = LoginForm()
    # context = {'form': form}
    # return render(request, 'auth/login_form.html', context)

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout Success')
    return redirect('/login')
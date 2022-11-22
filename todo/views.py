from django.shortcuts import render
from todo.forms import UserRegiterForm

def index(request):
    if request.method == 'POST':
        form = UserRegiterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('valid form')
            context = {'message': 'Registration Successful'}
        context = {'message': form.errors}
    else:
        form = UserRegiterForm()
        print('GET')
    context = {'form': form}
    
    return render(request, 'base.html', context)
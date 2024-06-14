# custom_app/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser
from .forms import CustomUserCreationForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = CustomUser.objects.filter(username=username).first()
            if user and user.check_password(password):
                request.session['user_id'] = user.id
                return redirect('home')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('home')

def home(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.get(id=user_id)
    else:
        user = None
    return render(request, 'home.html', {'user': user})

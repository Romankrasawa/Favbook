from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .forms import *
from .models import User
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required(login_url=reverse_lazy('home'))
def account(request):
    return render(request, template_name='user/account.html', context={'title':'Аккаунт'})

def profile(request, user_id):
    user = get_user_model()
    profile = get_object_or_404(user, slug = user_id)
    return render(request, template_name='user/profile.html', context={'profile': profile, 'title':f'Профіль користувача {profile.username}'})

def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(username, password, user)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('account'))
        else:
            return redirect(reverse_lazy('home'))
    print('ok')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username= username, email=email, password = password)
        print(user)
        return redirect(reverse_lazy('home'))

@login_required(login_url=reverse_lazy('home'))
def settings(request):
    if request.method == "POST":
        if request.FILES.get('photo'):
            request.user.photo = request.FILES.get('photo')
            request.user.save()
        return redirect(reverse_lazy('account'))
    else:
        form = SettingsUserForm(initial={'username':request.user.username,
                                         'email':request.user.email,
                                        })
        return render(request, template_name='user/settings.html', context = {'form':form, 'title':'Налаштування'})
@login_required(login_url=reverse_lazy('home'))
def log_out(request):
    logout(request)
    return redirect(reverse_lazy('home'))

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from Users.models import User
from Users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from Products.models import Basket
# Create your views here.


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request=request, user=user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'Users/login.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request=request, message='Поздравляем! Вы успешно зарегистрированы')
            return HttpResponseRedirect(reverse('Users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'Users/register.html', context=context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'title': 'Store - Профиль',
        'form': form,
        'Baskets': Basket.objects.filter(user=request.user),
    }
    return render(request, 'Users/profile.html', context)

@login_required
def logout(request):
    auth.logout(request=request)
    return HttpResponseRedirect(reverse('index'))

from django import forms
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .forms import SignUpForm, ProfileForm
from django.conf import settings
from django.views import generic
from django.contrib.auth.models import User
from .models import Profile
from django.shortcuts import render, redirect, get_object_or_404

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def our_games(request):
    return render(request, 'our_games.html', {})

def contact(request):
    return render(request, 'contactus.html', {})

def support(request):
    return render(request, 'support.html', {})

def promotion(request):
    return render(request, 'services_section.html', {})

def my_profile(request, pk=None, *args, **kwargs):
    try:
        profile_item = Profile.objects.get(pk=pk)
        prof_item = User.objects.get(pk=pk)
        profile_image = profile_item.image
        profile_username = prof_item.username
        profile_name = profile_item.full_name
        profile_email = prof_item.email
        profile_phone = profile_item.phone_number
        profile_balance = profile_item.balance
        profile_credit_amount = profile_item.credit_amount
        profile_ref = profile_item.ref_code
        context = {
            'profile_image' : profile_image,
            'profile_username' : profile_username,
            'profile_name': profile_name,
            'profile_email' : profile_email,
            'profile_phone':profile_phone,
            'profile_balance':profile_balance,
            'profile_credit_amount': profile_credit_amount,
            'profile_ref': profile_ref,
        }
        return render(request, 'my_profile.html', context)
    except Profile.DoesNotExist :
        profile_item = None
        context = {
            'profile_item': profile_item,
        }
        return render(request, 'my_profile.html', context)

def add_profile(request, pk=None, *args, **kwargs):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('my_profile', pk=pk)
    else:
        form = ProfileForm()
    return render(request, 'add_profile.html', {'form': form})

def help(request):
    context = {}
    return render(request, 'help.html', context)

def rewards(request):
    context = {}
    return render(request, 'rewards.html', context)

def demo(request):
    context = {}
    return render(request, 'demo.html', context)

def get_started(request):
    context = {}
    return render(request, 'get_started.html', context)

def show404(request):
    return render(request, '404.html')

def show500(request):
    return render(request, '500.html')



def user_set(request, pk=None, *args, **kwargs):
    return render(request, 'settings.html')
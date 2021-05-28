from apps.user.models import Buyer
from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            user_profile= Buyer(user=user)
            user_profile.save()
            return redirect ('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})

def profile(request):
    return render (request, 'profile.html')




from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request, 'main/mainpage.html')


def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/authorization')
    form = UserCreationForm()
    return render(request, 'main/registration.html', {'form': form})


def authorization(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/userpage')
        else: return redirect('/userpage')
    else:
        form = AuthenticationForm()
        return render(request, 'main/authorization.html', {'form': form})


def userpage(request):
    return render(request, 'main/userpage.html')

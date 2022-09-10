
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
import crypt
from main.models import LinkForm, Links


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
        else:
            return redirect('/userpage')
    else:
        form = AuthenticationForm()
        return render(request, 'main/authorization.html', {'form': form})


def userpage(request):
    if request.method == "POST":
        links = Links()
        links.originalLink = request.POST.get("link", "Undefined")
        # salt = crypt.mksalt(crypt.METHOD_MD5)
        # print('salt: ' + salt)
        hash = crypt.crypt(links.originalLink)
        links.hashLink = hash
        links.save()
        return redirect('/userpage')
    if request.method == "GET":
        return render(request, 'main/userpage.html', {'links': Links.objects.all()})

def link(request, link):
    print('link:  ' + link)
    if request.method == "POST":
        links = Links.objects.all()
        print(links)
        for l in links:
            print(l.hashLink + " " + link)
            if l.hashLink == link:
                red = l.originalLink
                return render(request, red)
    return render(request, 'main/mainpage.html')

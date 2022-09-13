
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
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
        while Links.objects.filter(hashLink = hash).exists():
            hash = crypt.crypt(links.originalLink)
        links.hashLink = hash
        links.save()
        return redirect('/userpage')
    if request.method == "GET":

        return render(request, 'main/userpage.html', {'links': Links.objects.all().order_by('count')})

def link(request, link):
    print('link:  ' + link)
    if request.method == "GET":
        link2 = Links.objects.get(hashLink=link)
        link2.count += 1
        link2.save()
        red = link2.originalLink
        return HttpResponseRedirect(red)
    if request.method == "POST":
        Links.objects.get(hashLink=link).delete()
        return redirect('/userpage')
    return render(request, 'main/mainpage.html')

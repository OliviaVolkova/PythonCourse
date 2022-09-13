from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
import crypt
from main.models import LinkForm, Links, UserForm


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
        form = UserForm(request.POST)
        if form.is_valid():
            print(form)
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            login(request, user)
            return redirect('/userpage')
        else:
            print(form)
            return redirect('/authorization')
    else:
        form = UserForm()
        return render(request, 'main/authorization.html', {'form': form})


def userpage(request):
    if request.method == "POST":
        links = Links()
        links.originalLink = request.POST.get("link", "Undefined")
        # salt = crypt.mksalt(crypt.METHOD_MD5)
        # print('salt: ' + salt)
        hash = crypt.crypt(links.originalLink).replace('?', 'F').replace('/', 'F')
        while Links.objects.filter(hashLink=hash).exists():
            hash = crypt.crypt(links.originalLink).replace('?', 'F').replace('/', 'F')
        links.hashLink = hash
        links.user = request.user.id
        links.save()
        return redirect('/userpage')
    if request.method == "GET":
        return render(request, 'main/userpage.html',
                      {'links': Links.objects.all().filter(user=request.user.id).order_by('count')})


def link(request, link):
    print('link:  ' + link)
    if request.method == "GET":
        try:
            link2 = Links.objects.filter(hashLink=link).get(user=request.user.id)
            link2.count += 1
            link2.save()
            red = link2.originalLink
            return HttpResponseRedirect(red)
        except:
            return redirect('/')
    if request.method == "POST":
        Links.objects.get(hashLink=link).delete()
        return redirect('/userpage')

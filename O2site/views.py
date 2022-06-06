from django.contrib.auth import authenticate, login, logout
import re
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from . import forms
from .models import Diaria, PessoaFisica, PessoaJuridica, Contrato, Servico, User



def index(request):
    return render(request, "index.html")

@login_required(login_url='login')
def cadastros(request):
    return render(request, "cadastros.html")

@login_required(login_url='login')
def diarias(request):
    form = forms.Diarias(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return HttpResponseRedirect('diarias')
    
    return render(request, "diarias.html", {"form":form, "diarias":Diaria.objects.all()})

@login_required(login_url='login')
def pessoafisica(request):
    form = forms.PessoaFisica(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return HttpResponseRedirect('pessoafisica')
    
    return render(request, "pfisica.html", {"form":form, "pessoas":PessoaFisica.objects.all()})

@login_required(login_url='login')
def pessoajuridica(request):
    form = forms.PessoaJuridica(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return HttpResponseRedirect('pessoajuridica')
    
    return render(request, "pjuridica.html", {"form":form, "pessoas":PessoaJuridica.objects.all()})

@login_required(login_url='login')
def contrato(request):
    form = forms.Contrato(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return HttpResponseRedirect('contrato')
    
    return render(request, "contrato.html", {"form":form, "contratos":Contrato.objects.all()})

@login_required(login_url='login')
def servico(request):
    form = forms.Servico(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return HttpResponseRedirect('servico')
    
    return render(request, "servico.html", {"form":form, "servicos":Servico.objects.all()})

def login_view(request):

    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "As senhas devem ser iguais"
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")

@login_required(login_url='login')
def update(request, item_id):

    if request.method == "GET":
        item = Diaria.objects.filter(id=item_id).first()
        form = forms.Diarias(instance=item)
        return render(request, "diarias.html", {"form":form, "diarias":Diaria.objects.all()})
    else: # POST request
        item = Diaria.objects.filter(id=item_id).first()
        form = forms.Diarias(request.POST, instance=item)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect(reverse('diarias'))   
        else:
            return render(request, "diarias.html", {"form":form, "diarias":Diaria.objects.all()})

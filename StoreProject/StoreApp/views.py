from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.models import User


from .models import Produit
from .forms import *

"""""
def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_produit')

else:
        form = LoginUserForm()
    return render(request, 'LoginUser.html', {'form': form})
"""""

# Create your views here.

def list_produit(request):
    pat = Produit.objects.all()
    return render(request, 'HomePage.html', {'pat': pat})






def login_user (request):
    if request.method == 'POST':
        username=request.POST['mail']
        password=request.POST['password']
        user=authenticate(request,username=username, password=password)
        if user is not None:
            msg = "success"
            login(request,user)
            return redirect('list_produit')
        else:
            msg="erreur"
            messages.success(request,"Error login. Try Again !!")
            return redirect('loginuser')
    else:
        form = LoginUserForm()
    return render(request, 'LoginUser.html', {'form': form})
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        email = request.POST['mail']
        password = request.POST['password']
        if form.is_valid():
            user = User.objects.create_user(username=email, email=email, password=password)
            form.save()
            user.save()
            return redirect('list_produit')
    else:
        form = UserForm()
    return render(request, 'AccountUser.html', {'form': form})


def create_product(request):
    if request.method=='POST':
        form=ProduitForm(request.POST)
        if form.is_valid():
            image_data = form.cleaned_data['image']
            image_model = Produit(image=image_data)
            form.save()
            return redirect('list_produit')
    else:
        form=ProduitForm()
    return render(request,'Produit.html',{'form':form})



from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Category


@login_required(login_url='/myapp/login/')  # redirect when user is not logged in
def show_category(request):
    user = request.user
    if request.method == "POST":
        search = request.POST.get('search')
        print(search)
        categories = Category.objects.filter(user=user, name__contains=search)
        return render(request, 'myapp/show_category.html', {'categories': categories})
    categories = Category.objects.filter(user=user)
    for cat in categories:
        print(cat.id)
    return render(request, 'myapp/show_category.html', {'categories': categories})


def home(request):
    return render(request, 'myapp/home.html')


import os
from django.contrib.auth.hashers import check_password


def edit_product(request, pk):
    prod = Category.objects.get(id=pk)
    print(prod.user.password)
    if check_password('admin1', prod.user.password):
        print("true")
    else:
        print("false")
    if request.method == "POST":
        os.remove(prod.image.path)
        prod.image = request.FILES['image']
        prod.name = request.POST.get('category')
        prod.save()
        return redirect('/myapp/show_category')
    return render(request, 'myapp/edit.html', {'prod': prod})


def delete_product(request, pk):
    # prod = Category.objects.get(id=pk)
    # os.remove(prod.image.path)
    # prod.delete()
    # return redirect('/myapp/show_category')
    if request.method == "POST":
        pk1 = request.POST.get('userid')
        pass1 = request.POST.get('password')
        prod = Category.objects.get(id=pk1)
        if check_password(pass1, prod.user.password):
            os.remove(prod.image.path)
            prod.delete()
            return redirect('/myapp/show_category')
        else:
            print("false")

    return render(request, 'myapp/delete.html', {'userid': pk})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('/myapp/login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'myapp/register.html', context)


def category(request):
    if request.method == 'POST':
        cat = Category()
        cat.name = request.POST.get('category')
        cat.user = request.user
        cat.image = request.FILES['image']
        cat.save()
        return redirect('/myapp/show_category')
    return render(request, 'myapp/category.html')

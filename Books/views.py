from django import forms
from django.shortcuts import redirect, render

from .models import *
# from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm

from django.contrib.auth.models import *

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


# wymagany -> from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def index(request):
    all_category = Category.objects.all()
    data = {'kategorie': all_category}

    # 'nazwa pliku który ma być wyświetlany,
    # słownik "data" który łączy zmienne w HTML z objektami django'
    # pliki HTML muszą być umieszczone w folderze szablonów "templates"
    return render(request, 'template.html', data)


@login_required(login_url='login')
def kategoria(request, id):
    category_user = Category.objects.get(pk=id)
    category_book = Books.objects.filter(category_id=category_user)
    all_category = Category.objects.all()
    data = {'category_user': category_user,
            'ksiazki': category_book,
            'kategorie': all_category}
    return render(request, 'book_category.html', data)


@login_required(login_url='login')
def books(request):
    book_user = Books.objects.all()
    data = {'ksiazki': book_user}
    return render(request, 'books.html', data)


@login_required(login_url='login')
def book(request, id):
    book_user = Books.objects.get(pk=id)
    all_category = Category.objects.all()
    data = {'book_user': book_user,
            'kategorie': all_category}
    return render(request, 'book.html', data)


@login_required(login_url='login')
def contactinfo(request):
    return render(request, 'contact.html')


@login_required(login_url='login')
def cart(request):
     if request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST.get('email')
        return render(request, 'cart.html')

    # context = {}
    # return render(request, 'cart.html', context)

    # if request.user.is_authenticated:
    #         if request.method == 'POST':
    #             email = request.POST.get('email')
    #         return render(request, 'cart.html')

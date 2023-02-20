"""Bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Books.views import *
# from Produkty.views import *
from Clients.views import clients

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', registerPage, name='register'),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name='logout'),

    path('', index, name='index'),
    # sciezka do kategoria/id, nazwa naszej funkcji ktora stwarzam w views.py,
    path('kategoria/<id>/', kategoria, name='kategoria'),
    path('ksiazka/<id>/', books, name='ksiazka'),
    path('books/', books, name='ksiazki'),
    path('book/<id>', book, name='ksiazka'),
    path('contact/', contactinfo, name='kontakt'),
    path('cart/', cart, name='koszyk'),
    #p ath('products/', produkt, name='produkty'),
    # path('produkty/<id>', produkt, name='produkt')
    path('client_list/<id>', clients, name='klient'),
    # path('Clients/', include('Clients.urls'), name='klient'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
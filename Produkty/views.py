from django.shortcuts import render
from django.http import HttpResponse
from .models import Produkty, Kategoria


def index(request):
    # wszystkie = Produkty.objects.all()
    # jeden = Produkty.objects.get(pk=2)
    # kat = Produkty.objects.filter(kategoria=1)
    # producent = Produkty.objects.filter(producent=3)
    # kat_name = Kategoria.objects.get(id=4)
    kategorie = Kategoria.objects.all()
    # null = Produkty.objects.filter(kategoria__isnull=False)
    # zawiera = Produkty.objects.filter(opis__icontains='karta')
    dane = {'kategorie' : kategorie}
    return render(request, 'szablon.html', dane)

def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_produkt = Produkty.objects.filter(kategoria = kategoria_user)
    kategorie = Kategoria.objects.all()
    dane = {'kategoria_user' : kategoria_user,
            'kategoria_produkt' : kategoria_produkt,
            'kategorie' : kategorie }
    return render(request, 'kategoria_produkt.html', dane)

def produkt(request, id):
    produkt_user = Produkty.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    dane = {'produkt_user': produkt_user, 'kategorie' : kategorie }
    return render(request, 'produkt.html', dane )

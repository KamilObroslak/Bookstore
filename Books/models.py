from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    def __str__(self):
        return self.category_name

    category_name = models.CharField(max_length=60)
    category_desc = models.TextField(blank=True)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"


class Books(models.Model):
    def __str__(self):
        return self.title

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Ksiażka"
        verbose_name_plural = "Ksiażki"

# class Cart(models.Model):
#     def __str__(self):
#         return self.price_total
    
#     email_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     id_book = models.CharField(max_length=100)
#     quantity = models.CharField(max_length=10)
#     price_total = models.DecimalField(max_digits=12, decimal_places=2)

#     def buyer():
#         buyer_email = ???
    
#     class Meta:
#         verbose_name = "Koszyk"
#         verbose_name_plural = "Koszyki"
        

# ------------------Dodatkowe aplikacje---------------------------

class Clients_info(models.Model):
    def __str__(self):
        return self.client_name

    client_name = models.CharField(max_length=60)
    client_surname = models.CharField(max_length=60)
    client_email = models.CharField(max_length=60)
    client_phone = models.CharField(max_length=16)

    class Meta:
        verbose_name = "klient"
        verbose_name_plural = "klienci"


class Producent(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=60)
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name = "Producent"
        verbose_name_plural = "Producenci"

class Kategoria(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

class Produkty(models.Model):
    def __str__(self):
        return self.nazwa + " "

    kategoria = models.ForeignKey(Kategoria, null=True, blank=True, on_delete=models.CASCADE)
    producent = models.ForeignKey(Producent,on_delete=models.CASCADE,null=True)
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

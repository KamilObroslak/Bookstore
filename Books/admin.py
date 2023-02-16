from django.contrib import admin
from .models import Books, Category
from Produkty.models import Producent, Produkty, Kategoria
from Clients.models import Clients_info

admin.site.register(Books)
admin.site.register(Category)
admin.site.register(Producent)
admin.site.register(Produkty)
admin.site.register(Kategoria)
admin.site.register(Clients_info)

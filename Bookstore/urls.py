from django.contrib import admin
from django.urls import path, include
from Books.views import *
# from Produkty.views import *
from Clients.views import clients

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'books', BookViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', registerPage, name='register'),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name='logout'),
    path('', index, name='index'),
    path('kategoria/<id>/', kategoria, name='kategoria'),
    path('ksiazka/<id>/', books, name='ksiazka'),
    path('books/', books, name='ksiazki'),
    path('book/<id>', book, name='ksiazka'),
    path('contact/', contactinfo, name='kontakt'),
    path('cart/', cart, name='koszyk'),
    path('client_list/<id>', clients, name='klient'),
    path('checkout/', checkout, name='checkout'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
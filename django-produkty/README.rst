{\rtf1}

=====
Produkty
=====

Description

Quick start
-----------

1. Add "Produkty" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'Produkty',
    ]

2. Include the Produkty URLconf in your project urls.py like this::

    path('Produkty/', include('Produkty.urls')),

3. Run ``python manage.py migrate`` to create the Produkty models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a Produkt (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/Produkty/ to participate in the Produkt.
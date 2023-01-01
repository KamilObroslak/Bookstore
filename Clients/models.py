from django.db import models

class Clients_info(models.Model):
    # def __str__(self):
    #     return self.client_name

    client_name = models.CharField(max_length=60)
    client_surname = models.CharField(max_length=60)
    client_email = models.CharField(max_length=60)
    client_phone = models.CharField(max_length=16)

    class Meta:
        verbose_name = "Klient"
        verbose_name_plural = "Klienci"

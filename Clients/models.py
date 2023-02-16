from django.db import models

class Clients_info(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=16)

    class Meta:
        verbose_name = "klient"
        verbose_name_plural = "klienci"

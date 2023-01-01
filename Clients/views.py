from django.shortcuts import render
from .models import Clients_info


def clients(request, id):
    client_user = Clients_info.objects.get(pk=id)
    data = {'client_user': client_user}
    return(request,'client_list.html', data)

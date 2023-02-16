from django.shortcuts import render
from .models import Clients_info


def clients(request, id):
    client_user = Clients_info.objects.get(pk=id)
    # import pdb;
    # pdb.set_trace()
    data = {'client_user': client_user}
    return render(request, 'client_list.html', data)

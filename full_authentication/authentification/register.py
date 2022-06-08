from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        nomutil = request.POST['nomutil']
        email = request.POST['email']
        mdp = request.POST['mdp']
        mdp1 = request.POST['mdp1']

        mon_util = User.objects.create(email)
        mon_util.first_name = nom
        mon_util.last_name = prenom
        mon_util.username = nomutil
        mon_util.password = mdp
        mon_util.save()

    return render(request, "full_authentication/register.html")

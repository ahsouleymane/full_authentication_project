from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        this_user = User.objects.get(username = username)

        if user is not None:
            auth_login(request, user)
            prenom = user.first_name
            return render(request, "full_authentication/manage_partners_health.html", {'prenom': prenom})
        elif this_user.is_active == False:
            messages.error(request, 'S\'il vous plait veuillez activer votre compte avant de vous connectez !!!')
        else:
            messages.error(request, 'Nom utilisateur ou mot de passe incorrect !!!')
            return redirect('login')

    return render(request, "full_authentication/login.html")

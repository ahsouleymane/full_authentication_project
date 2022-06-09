from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        mon_util = User.objects.create_user(username, email, password)
        mon_util.first_name = nom
        mon_util.last_name = prenom
        mon_util.save()
        messages.success(request, 'Votre compte a été crée avec succès !!!')
        return redirect('login')

    return render(request, "full_authentication/register.html")

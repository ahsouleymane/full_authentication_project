from pickle import FALSE
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from full_authentication_project import settings
from django.core.mail import send_mail, EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from full_authentication.token import generatorToken

# Create your views here.

def register(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if User.objects.filter(username = username):
            messages.error(request, 'Cet nom d\'utilisateur existe déja !!!')
            return redirect('register')

        elif User.objects.filter(email = email):
            messages.error(request, 'Cet Email a déja un compte !!!')
            return redirect('register')

        elif password != password1:
            messages.error(request, 'Echec de confirmation du mot de passe !!!')
            return redirect('register')

        elif not username.isalnum():
            messages.error(request, 'Le nom d\'utilisateur n\'est pas alphanumerique !!!')
            return redirect('register')

        mon_util = User.objects.create_user(username, email, password)
        mon_util.first_name = nom
        mon_util.last_name = prenom
        mon_util.is_active = False
        mon_util.save()

        # Sending welcome Email after account creation

        messages.success(request, 'Votre compte a été crée avec succès !!!')
        wel_subject = "Soyez les bienvenus sur notre site web !!!"
        wel_message = "Assalamou Alaykoum" + " " + nom + " " + prenom + "\n\n Nous sommes heureux de vous comptez parmis nos abonnés. \n\n Nous vous remercions pour votre confiance ! \n\n SANCFIS \n\n"
        from_email = settings.EMAIL_HOST_USER
        to_list = [mon_util.email]
        send_mail(wel_subject, wel_message, from_email, to_list, fail_silently=FALSE)
        
        # Sending confirmation Email for account creation

        current_site = get_current_site(request)
        conf_subject = "Confirmation de la création de votre compte !!!"
        conf_message = render_to_string("full_authentication/conf_email.html", {
            'name': nom,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(mon_util.pk)),
            'token': generatorToken.make_token(mon_util),
        })

        email = EmailMessage(
            conf_subject,
            conf_message,
            settings.EMAIL_HOST_USER,
            [mon_util.email],
        )

        email.fail_silently = False
        email.send()

        return redirect('login')

    return render(request, "full_authentication/register.html")

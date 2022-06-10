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


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and generatorToken.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Félicitation !!!  votre compte a été crée avec succès !!!")
        return redirect('login')
    else:
        messages.error(request, "Erreur lors de la céation de votre compte, Réessayer !!!")
        return redirect('register')
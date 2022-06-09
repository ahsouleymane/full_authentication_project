from django.shortcuts import render

# Create your views here.

def logout(request):
    return render(request, 'full_authentication/login.html')

from django.urls import path
from full_authentication.authentification import bonjour,register,login,logout, account_activate

urlpatterns = [
    path('', bonjour.home, name='home'),
    path('register/', register.register, name='register'),
    path('login/', login.login, name='login'),
    path('logout/', logout.logout, name='logout'),
    path('activate/<uidb64>/<token>', account_activate.activate, name='activate')
]

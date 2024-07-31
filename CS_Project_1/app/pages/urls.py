from django.urls import path

from .views import homePageView,registerPageView,RegisterFormView,custom_login,loginPageView,transfer

urlpatterns = [
    path('', homePageView, name='home'),
    path('register', registerPageView, name='register'),
    path('register_form', RegisterFormView, name='register_form'),
    path('process_form',custom_login,name='process_form'),    
    path('login',loginPageView,name='login'),
    path('transfer_form',transfer,name='transfer_form')
    
]


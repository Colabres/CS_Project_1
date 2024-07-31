from django.urls import path

from .views import homePageView,registerPageView,RegisterFormView,loginPageView,transfer,loginView
#from .views import custom_login
urlpatterns = [
    path('', homePageView, name='home'),
    path('register', registerPageView, name='register'),
    path('register_form', RegisterFormView, name='register_form'),
    #path('process_form',custom_login,name='process_form'),
    path('process_form',loginView,name='process_form'),    
    path('login',loginPageView,name='login'),
    path('transfer_form',transfer,name='transfer_form')
    
]


from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import connection
from .models import App_users, Account
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import random

# @login_required
def homePageView(request):
    #V1
    # user_id = request.session['user_id']
    # app_user = App_users.objects.get(id=user_id)
    # balance = app_user.balance
    #V2
    account = Account.objects.get(user=request.user)
    balance = account.balance
    ################################################
    context = {'balance': balance,'username':request.user.username}    
    return render(request, 'pages/home.html', context)

def registerPageView(request):
    return render(request, 'pages/register.html')

def loginPageView(request):
    return render(request, 'pages/login.html')

@csrf_exempt
def RegisterFormView(request):
    if request.method == 'POST':          
        newusername = request.POST.get('username')
        newpassword = request.POST.get('password')
        newBalance = 100
        newAccNum = random.randint(1000, 9999)

        # This line registers a new user using a custom model and saves both the user and their account to the same table.
        # App_users.objects.create(username=newusername, password=newpassword, account_number=newAccNum, balance=newBalance)
        # return redirect('home')
        # return render(request, 'register.html')
          
        # This is for non-vulnerable version.
        # Validating password 
        try:
            validate_password(newpassword)
            user = User.objects.create_user(username=newusername, password=newpassword)
            Account.objects.create(user=user, account_number=newAccNum, balance=newBalance)
            #this is for v1
            user = App_users.objects.get(username=newusername) 
            request.session['user_id'] = user.id
            #this is for v2
            return redirect('home')
        except ValidationError as e:
            errors = list(e.messages)
            return render(request, 'pages/register.html', {'errors': errors})

    return render(request, 'pages/register.html')
#V1 login
# @csrf_exempt
# def custom_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         try:
#             user = App_users.objects.get(username=username)
#             if user.password == password:
#                 request.session['user_id'] = user.id
#                 return redirect('home')  
#             else:
#                 return HttpResponse("Invalid credentials", status=401)
#         except App_users.DoesNotExist:
#             return HttpResponse("User does not exist", status=404)

#     return render(request, 'login.html')
#V2 login
@csrf_exempt
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid username or password", status=403)
    
    return render(request, 'pages/login.html')
#transfer V1
@csrf_exempt
def transfer(request):
    if request.method == 'POST':
        user_from = request.POST.get('from')
        user_to = request.POST.get('to')
        amount = int(request.POST.get('amount'))
        try:
            user_from = App_users.objects.get(username=user_from)
            
            with connection.cursor() as cursor:
                cursor.execute(f"UPDATE app_users SET balance = balance - {amount} WHERE username = '{user_from}'")
                
            # user_from.balance -= amount
            # user_from.save()
            user_to = App_users.objects.get(username=user_to)
            user_to.balance += amount
            user_to.save()
            return redirect('home')
            
        except App_users.DoesNotExist:
            return HttpResponse("User does not exist", status=404)

#transfer V2
#@csrf_exempt
def transfer(request):
    if request.method == 'POST':
        #this fix the desing problem.
        user_from = Account.objects.get(user=request.user)
        user_to = Account.objects.get(user=User.objects.get(username=request.POST.get('to'))) 
        amount = int(request.POST.get('amount'))
        
        try:                   
                
            user_from.balance -= amount
            user_from.save()

            user_to.balance += amount
            user_to.save()
            return redirect('home')
            
        except App_users.DoesNotExist:
            return HttpResponse("User does not exist", status=404)
		
            
        

		

            

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
#from django.contrib.auth.models import App_users
from .models import App_users
import random






#@login_required
def homePageView(request):

	return render(request, 'pages/home.html')

def registerPageView(request):

	return render(request, 'pages/register.html')
def loginPageView(request):

	return render(request, 'pages/login.html')
@csrf_exempt
def RegisterFormView(request):
	if request.method == 'POST':
		newusername = request.POST.get('username')
		newpassword = request.POST.get('password')
		newBalance  = 100
		newAccNum= random.randint(1000, 9999)
		#print(newusername,newpassword)
		App_users.objects.create(username=newusername, password=newpassword,account_number=newAccNum,balance=newBalance)

		return redirect('home')  
	
	return render(request, 'register.html')

@csrf_exempt
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = App_users.objects.get(username=username)
            if user.password == password:
                
                request.session['user_id'] = user.id
                return redirect('home')  
            else:
                return HttpResponse("Invalid credentials", status=401)
        except App_users.DoesNotExist:
            return HttpResponse("User does not exist", status=404)

    return render(request, 'login.html')

@csrf_exempt
def transfer(request):
    if request.method == 'POST':
        user_from = request.POST.get('from')
        user_to = request.POST.get('to')
        ammount = int(request.POST.get('ammount'))
        try:
            user_from = App_users.objects.get(username=user_from)
            user_from.balance+=ammount
            user_from.save()
            user_to = App_users.objects.get(username=user_to)
            user_to.balance+=ammount
            user_to.save()
            return redirect('home')            
			
        except App_users.DoesNotExist:
            return HttpResponse("User does not exist", status=404)
            
		

        
		
        
		
            
        

		

            

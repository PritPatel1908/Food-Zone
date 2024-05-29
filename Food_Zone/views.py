from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from Food_Zone.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from Food_Zone.EmailBackEnd import EmailBackEnd
from django.contrib import messages

# Create your views here.
def index(request):
    # if request.user.is_authenticated:
    #     if request.user.user_type == 1:
    #         return render(request, 'Admin/Home Profile/index.html')
    #     else:
    #         check_account = request.session.get('vendor_account')
    #         if check_account == True:
    #             return render(request, 'Vendor/Home Profile/index.html')
    #         else:
    #             products = Product.objects.all().order_by('date')
    #             categories = Category.objects.all().order_by('date')
    #             context = {
    #                 'products': products,
    #                 'categories' : categories
    #             }
    #             return render(request, 'User/index.html', context)
    # else:
    #     products = Product.objects.all().order_by('date')
    #     categories = Category.objects.all().order_by('date')
    #     context = {
    #         'products': products,
    #         'categories' : categories
    #     }
    #     return render(request, 'User/index.html', context)
    return render(request, 'file:///D:/new/Templates/Nest_v5.7_Unzip-First/nest-frontend/index-3.html')

# Signup
# Signup Page
def signup_page(request):
    return render(request, 'signup.html')
    
# Signup 
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        try:
            user = Users.objects.get(email = email)
            if user.username == username:
                return JsonResponse({'status': 400, 'error': 'Your username is already used try new username.'})
            if user.email == email:
                return JsonResponse({'status': 400, 'error': 'Your email is already used try new email.'})
        except Users.DoesNotExist:
            if len(password) < 8:
                return JsonResponse({'status': 400, 'error': 'Password must be at least 8 characters long.'})

            if password != cpassword:
                return JsonResponse({'status': 400, 'error': 'Password and Confirm Password do not match.'})
        
            user = Users(
                username = username,
                email = email,
                password = make_password(password)
            )
            user.save()

            return JsonResponse({'status': 200})
    return redirect('signup_page')

# Signin
# Signin Page
def signin_page(request):
    return render(request, 'signin.html')

# Signin
def signin(request):
    if request.method == 'POST':
        usernameoremail=request.POST.get('usernameoremail')
        password=request.POST.get('password')

        if len(password) < 8:
            return JsonResponse({'status': 400, 'error': 'Password must be at least 8 characters long.'})

        user = EmailBackEnd.authenticate(request, usernameoremail, password)

        if user is not None: 
            login(request, user)
            user_type = user.user_type
            if user_type == 1:
                return JsonResponse({'status': 200})
            elif user_type == 2:
                if '@' in usernameoremail:
                    messages.success(request, "You are logged in.")
                    return JsonResponse({'status': 201})
                elif 'ven' in usernameoremail:
                    request.session['vendor_account'] = True
                    return JsonResponse({'status': 202})
                else:
                    messages.success(request, "You are logged in.")
                    return JsonResponse({'status': 201})
            else:
                return JsonResponse({'status': 400, 'error': 'You have not created account so first create account !'})
        else:
            return JsonResponse({'status': 400, 'error': 'Email / Username or Password are invalid !!'})
    return redirect('signin_page')

# Logout
def logout(request):
    django_logout(request)
    messages.warning(request, "You are logged out.")
    return redirect('index')

def favicon(request):
    return HttpResponse("", content_type="image/x-icon")
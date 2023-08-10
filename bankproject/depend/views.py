from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login as auth_login



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if not username or not password or not cpassword:
            #messages.error(request, "Please fill in all the fields.")
            return redirect('depend:register')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Successfully Registered")
                return redirect('depend:login')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "Registration successful. Please log in.")
                return redirect('depend:login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('depend:register')

    return render(request, "register.html")

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
        # Handle user registration here
        # You can access the submitted data using request.POST dictionary
            return redirect('bankapp:postlogin')# Redirect to login page after successful registration
        else:
            messages.info(request,'invalid entry')
            return redirect('depend:login')
    return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/home/homepage')
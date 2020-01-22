from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .models import UserMessage


def create_account(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            if password == confirm_password:
                if User.objects.filter(email=email).exists():
                    messages.error(
                        request, 'This email is already used by existing account. Please use another email')
                    return redirect('home_view')
                else:
                    if User.objects.filter(username=username).exists():
                        messages.error(
                            request, 'This username already exists. Please user another username. Or, if this is your username, log in to your account.')
                        return redirect('home_view')
                    else:
                        user = User.objects.create_user(
                            first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                        user.is_active = True
                        user.save()
                        messages.success(
                            request, 'Thank you for creating your account. Please log in now.')
                        return redirect('home_view')
            else:
                messages.error(request, 'passwords do not match')
                return redirect('home_view')

        else:
            return redirect('home_view')
    else:
        messages.error(request, 'Only new users can create new account')
        return redirect('home_view')


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(
                    request, 'Welcome! You have successfully logged in')
                return redirect('home_view')
            else:
                messages.error(
                    request, 'We are sorry! Credentials do not match. Try again')
                return redirect('home_view')
        else:
            return redirect('home_view')
    else:
        return redirect('home_view')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(
            request, 'You have successfully logged out. Thank you for visiting.')
        return redirect('home_view')
    else:
        return redirect('home_view')


def send_message(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            name = user.get_full_name()
            email = user.email
            subject = request.POST['subject']
            message = request.POST['message']
            user_message = UserMessage(
                name=name, email=email, subject=subject, message=message)
            user_message.save()
            messages.success(
                request, 'Thank you for your message. We will get back to you the soonest')
            return redirect('home_view')
        else:
            return redirect('home_view')
    else:
        messages.error(
            request, 'You need to be logged in to send message and inquiries')
        return redirect('home_view')

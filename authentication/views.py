from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from authentication.auth.login import Login


# Create your views here.
def login(request):
    global password, username
    form = Login()
    context = {
        form: form,
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if user.is_superuser or user.is_staff:
                messages.success(request, "Successfully Logged Out")
                return redirect('dashboard')
            else:
                return redirect('user_dashboard')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("index")
    else:
        return render(request, "authentication/templates/login.html", context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # Authenticate the user
            user = authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return redirect('dashboard')
    else:
        initial_data = {'username': '', 'email': '', 'password1': '', 'password2': ''}
        form = UserCreationForm(initial=initial_data)
    return render(request, "authentication/templates/register.html", {"form": form})


@login_required(login_url='index')
def dashboard(request):
    return render(request, "authentication/templates/dashboard.html")


def handle_logout(request):
    logout(request)
    return redirect('index')

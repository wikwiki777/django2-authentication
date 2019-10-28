from django.shortcuts import render, redirect, reverse
# Imports for authentication
from django.contrib import auth, messages


# Create your views here.
def index(request):
    """
    Return the index.html file
    """
    return render(request, 'index.html')


def logout(request):
    """
    Log the user out
    """
    auth.logout(request)
    messages.success(request, 'You have successfully been logged out!')
    # Reverse allows us to pass
    # name of url io of name of view
    return redirect(reverse('index'))


def login(request):
    """
    Return a login page
    """
    return render(request, 'login.html')

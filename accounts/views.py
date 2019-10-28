from django.shortcuts import render, redirect, reverse
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
# Imports for authentication
from django.contrib import auth, messages


# Create your views here.
def index(request):
    """
    Return the index.html file
    """
    return render(request, 'index.html')


@login_required
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
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()

    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Render the registration page"""
    registration_form = UserRegistrationForm()
    return render(request, 'registration.html',
                  {'registration_form': registration_form})

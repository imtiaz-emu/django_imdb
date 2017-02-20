from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete')

    else:
        form = UserRegistrationForm()

    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('authentication/registration_form.html', token)


def registration_complete(request):
    return render_to_response('authentication/registration_complete.html')

def login_user(request):
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/movies')


    return render(request, 'authentication/login.html')


def loggedin(request):
    return render_to_response('authentication/loggedin.html',
                              {'username': request.user.username})
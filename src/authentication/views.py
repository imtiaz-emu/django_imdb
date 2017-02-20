from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm
from django.core.context_processors import csrf


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

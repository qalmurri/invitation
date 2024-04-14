from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render
from .forms import ClientUserForm, ClientPasswordForm

def signin(request):
    template = loader.get_template('signin.html')
    return HttpResponse(template.render())

def signup(request):
    user_form = ClientUserForm(request.POST or None)
    password_form = ClientPasswordForm(request.POST or None)

    if user_form.is_valid() and password_form.is_valid:
        user_form.save()
        password_form.save()

    context = {'user_form': user_form, 'password_form': password_form}
    return render(request, 'signup.html', context)
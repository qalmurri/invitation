from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ClientRegistrationForm

#def signin(request):
#    template = loader.get_template('signin.html')
#    return HttpResponse(template.render())

def registration_view(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Tampilkan pesan sukses atau redirect ke halaman lain
    else:
        form = ClientRegistrationForm()
    return render(
        request,
        'signup.html',
        {'register': form})
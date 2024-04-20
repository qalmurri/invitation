from django import forms
from django.http import request

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from .models import ClientUser, ClientPassword, ClientSetting, ClientLast

class ClientRegistrationForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if ClientUser.objects.filter(
            username = username
            ).exists():
            raise forms.ValidationError("Username sudah ada, pilih yang lain.")
        return username

    def save(self, commit = True):
        default = 0

        client_id = ClientUser.objects.create(
            username = self.cleaned_data['username']
            )
        
        ClientPassword.objects.create(
            client = client_id,
            password = self.cleaned_data['password']
            )
        
        ClientSetting.objects.create(
            client = client_id,
            mode = default
            )
        
        ClientLast.objects.create(
            client = client_id,
            language = default,
            platform = default,
            agent = default,
            ip = default
            )

        return client_id
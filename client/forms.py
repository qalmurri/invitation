from django import forms
from .models import ClientUser, ClientPassword

class ClientUserForm(forms.ModelForm):
    class Meta:
        model = ClientUser
        fields = [
            "username",
            "firstname",
            "lastname"
        ]

class ClientPasswordForm(forms.ModelForm):
    class Meta:
        model = ClientPassword
        fields = [
            "password",
            "passwordlevel",
        ]
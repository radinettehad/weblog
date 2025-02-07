
from django import forms
from django.contrib.auth import password_validation
from .models import CustomUser


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')

    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        password1 = self.cleaned_data.get("password")
        password_validation.validate_password(password1)
        return password1


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
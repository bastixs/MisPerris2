from django import forms
from .models import Dueño, Mascota
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class DueñoForm(forms.ModelForm):
    class Meta:
        model = Dueño
        fields = ('nombre',)


class Mascotaform(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ('nombre', 'raza', 'descripcion', 'dueño')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

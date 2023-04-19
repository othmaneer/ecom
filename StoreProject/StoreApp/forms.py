from django import forms
from .models import *


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix', 'quantite', 'image']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ImageField(),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nom', 'prenom', 'ddn', 'mail', 'password', 'phone']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'ddn': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                       }),
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),

        }


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['mail', 'password', ]
        widgets = {
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

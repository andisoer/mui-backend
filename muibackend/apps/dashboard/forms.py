#from django import forms
#from django.contrib.auth.forms import AuthenticationForm

#class LoginForm(AuthenticationForm):
#    username = forms.CharField(
#        label="Username",
#        max_length=30,
#        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'})
#    )
#    password = forms.CharField(
#        label="Password",
#        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
#    )

#    # Jika diperlukan, Anda dapat menambahkan metode atau validasi kustom di sini
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    name = forms.CharField(max_length=100, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    photo = forms.ImageField(required=False) 
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'name', 'photo']  
 

class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(
        max_length=234,
        required=True,
        help_text='Required. Enter a valid email address.',
    )
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        

from django import forms
from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email']

class PreferencesForm(forms.Form):
    email_notifications = forms.BooleanField(required=False)
    dark_mode = forms.BooleanField(required=False)
    
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'




from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpFrom(UserCreationForm):
    email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput())
    first_name= forms.CharField(max_length=20,required=True)

    class Meta:
        # للحفظ
        model=User
        fields = ['username','first_name','last_name','email','password1','password2']

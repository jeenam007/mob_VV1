from django.contrib.auth.models import User
from django.forms import ModelForm 
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control p-2"}),
            "last_name":forms.TextInput(attrs={"class":"form-control p-2"}),
            "email":forms.EmailInput(attrs={"class":"form-control p-2"}),
            "username":forms.TextInput(attrs={"class":"form-control p-2"}),
            "password1":forms.CharField(widget=forms.PasswordInput),
            "password2":forms.CharField(widget=forms.PasswordInput),
        }
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields["first_name"].required = True
            self.fields["email"].required = True
            # self.fields["email"].widget.attrs.update({'class': 'form-control p-2'})

class LoginForm(forms.Form):
        username=forms.CharField()
        password=forms.CharField(widget=forms.PasswordInput)


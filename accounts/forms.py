from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from users. models import Student,Admin

class SignupForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(UserCreationForm,self).__init__(*args,**kwargs)
        for field in ['first_name','last_name','username','password1','password2']:
            self.fields[field].help_text = None
            self.fields[field].required = True
    def clean_email(self):
        email = self.cleaned_data['email']
        check = User.objects.filter(email=email).exists()
        if check:
            raise ValidationError('Email already exists')
        return email
    class Meta():
        model=User
        fields=('first_name','last_name','username','email','password1','password2')

class StudentForm(forms.ModelForm):
    class Meta():
        model= Student
        fields= ('phone_number','bio','profile_pic')

class AdminForm(forms.ModelForm):
    class Meta():
        model= Admin
        fields= ('phone_number','bio','profile_pic')
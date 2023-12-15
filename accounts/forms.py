from dataclasses import field
from pyexpat import model
from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    """
    A form for user registerion 
    """
    password1 = forms.CharField(label='password' , widget= forms.PasswordInput)
    password2 = forms.CharField(label='confirm password' , widget= forms.PasswordInput)
    
    class Meta:
        model = CustomUser
        fields = ('email' ,'full_name' , 'phone_number')
        
    def clean_password2(self):
        """
        password check
        """
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError ('password is not match')
        return cd['password2']
    
    def save(self, commit=True):
        user =  super().save(commit=False)
        user.set_password(self.changed_data['password1'])
        if commit:
            user.save()
        return user
    
    
class UserChangeForm(forms.ModelForm):
    """
    cheange user info 
    """
    password = ReadOnlyPasswordHashField(help_text="you can change password using <a href=\"../password/\">this form</a>.")
    
    class Meta:
        model = CustomUser
        fields = ('email' ,'full_name' , 'phone_number' , 'last_login')
    
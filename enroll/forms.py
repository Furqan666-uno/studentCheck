from django import forms
from .models import User

class studentRegisteration(forms.ModelForm):
    class Meta:
        model= User
        fields= ['name', 'email', 'password']
        widgets= { # widgets are used for giving bootstrap properties to form 
            'name':forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'id':'emailid'}),
            'password':forms.PasswordInput(attrs={'class':'form-control', 'id':'passwordid'}), 
        }


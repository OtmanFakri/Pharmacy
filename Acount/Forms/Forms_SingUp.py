from ..models import Utilisateur2
from django import forms

class SignUpForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Utilisateur2
        
        fields = ['Real_name', 
                    'Email', 
                    'Password',
                    'confirm_password', 
                    'Type_counte', 
                ]
        widgets = {
            'Type_counte': forms.RadioSelect(choices=[(True, 'Pharmacy'), (False, 'Normal')]),
        }       
        def clean(self):
            cleaned_data = super(SignUpForm, self).clean()
            Password = cleaned_data.get("Password")
            confirm_password = cleaned_data.get("confirm_password")
            #gender = cleaned_data.get("Type_counte")

            if Password != confirm_password:
                raise forms.ValidationError(
                    "password and confirm_password does not match"
                )
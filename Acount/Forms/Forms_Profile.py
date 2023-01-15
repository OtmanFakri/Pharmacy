from ..models import Utilisateur2
from django import forms
class MyModelForm(forms.ModelForm):
    class Meta:
        model = Utilisateur2
        fields = '__all__'
        

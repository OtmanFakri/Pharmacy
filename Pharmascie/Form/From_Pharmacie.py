from ..models import Pharmacie
from Acount.models import Utilisateur2 

from django import forms



class AuthorChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        if obj.id == 1:
            return obj.Real_name
        return None

class From_Pharmacie(forms.ModelForm):

    class Meta:
        model = Pharmacie
        
        exclude = '__all__'
        #exclude=['idutil']

        widgets = {
            'sidegarde': forms.RadioSelect(choices=[(True, 'pharmacie de gard'), (False, 'No')]),   
        }




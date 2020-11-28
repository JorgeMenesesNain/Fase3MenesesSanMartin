from django import forms

from . models import Compañia

class CompañiaForm(forms.ModelForm):
    compañia = forms.CharField(label='Compañia',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))

    class Meta:
        model = Compañia
        fields = ('compañia',)
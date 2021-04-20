from django import forms
from .models import Contact ,Comment


class FormContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name'    : forms.TextInput(attrs={'class' : 'form-control'}),
            'email'   : forms.EmailInput(attrs={'class':'form-control'}),
            'message' : forms.Textarea(attrs={'class' : 'form-control'})
        }



class FormComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)       
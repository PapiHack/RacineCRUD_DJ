from django import forms
from .models import User

class UserForm(forms.ModelForm):
    mdp = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = '__all__'
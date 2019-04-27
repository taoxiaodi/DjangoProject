from django import forms
from .models import User
#
# class CreatForm(forms.Form):
#     title = forms.CharField()
#     datetime = forms.DateTimeField()


class CustomForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username', 'password']

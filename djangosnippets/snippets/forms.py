from django import forms
from django.models import Sunippet


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Sunippet
        fields = ('title', 'code', 'descrption')

from django import forms
from .models import *

# create new forms
class URLShortenerForm(forms.ModelForm):
    class Meta:
        model = URLShortener
        fields = ['url']


        
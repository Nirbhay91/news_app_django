
from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['name', 'description', 'date', 'author', 'image', 'source']

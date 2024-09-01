from django import forms
from .models import Comment


class Comments(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'text')
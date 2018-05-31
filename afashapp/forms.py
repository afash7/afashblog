from .models import Post
from django import forms

class Postform (forms.ModelForm):
    class Meta:
        models = Post
        feilds = (
            'title',
            'text',
        )

        

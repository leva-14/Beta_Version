from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title' ,'text', 'data', 'author_id')
        widgets = {
            'title': forms.TextInput(attrs={ 'placeholder':'Title', 'class': 'input-form'}),
            'text': forms.TextInput(attrs={'placeholder':'Text', 'class': 'input-form'}),
        }

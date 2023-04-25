from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Название статьи', widget=forms.TextInput())
    text = forms.CharField(label="Описание статьи", widget=forms.Textarea())

    class Meta:
        model = Post
        fields = ('title', 'text',)

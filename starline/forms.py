from django import forms
from pkg_resources import _

from starline.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'numbers_phone', 'body')
        widgets = {'numbers_phone': forms.TextInput(attrs={'type': 'tel',
                                                           'placeholder': '+375 (__)___-__-__',
                                                           'value': '+375'})}

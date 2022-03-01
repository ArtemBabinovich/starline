from django import forms
from pkg_resources import _
from starline.models import Comment
from django.contrib.auth.forms import AuthenticationForm
from django.forms import forms
from .models import Feedback

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'numbers_phone', 'body')
        widgets = {'numbers_phone': forms.TextInput(attrs={'type': 'tel',
                                                           'placeholder': '+375 (__)___-__-__',
                                                           'value': '+375'})}


class FeedbackForm(forms.Form):

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'phone', 'message')

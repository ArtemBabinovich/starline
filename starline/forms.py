from django import forms
from starline.models import Comment, Feedback


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'numbers_phone', 'body')
        widgets = {'numbers_phone': forms.TextInput(attrs={'type': 'tel',
                                                           'placeholder': '+375 (__)___-__-__',
                                                           'value': '+375'})}


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'phone', 'message')


from django import forms
from starline.models import Comment, Feedback


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'numbers_phone', 'body')
        widgets = {'numbers_phone': forms.TextInput(attrs={'type': 'tel',
                                                           'placeholder': '+375 (__)___-__-__',
                                                           'value': '+375'})}

<<<<<<< HEAD



class FeedbackForm(forms.Form):
    # name = forms.CharField(label='Имя', max_length=100)
    # email = forms.EmailField(label='Почта')
    # phone = forms.CharField(label='Телефон', max_length=100)
    # message = forms.TextField(label='Сообщение')
=======
>>>>>>> 603e0b1ad91754a28fc0e87dbe72b219d894f7e6

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'phone', 'message')


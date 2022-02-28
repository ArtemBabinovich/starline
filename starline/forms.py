from django.contrib.auth.forms import AuthenticationForm
from django.forms import forms
from .models import Feedback


# class UserLoginForm(AuthenticationForm): #AuthenticationForm #forms.Form
#     username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'style': 'margin:10px; padding:10px; height:40px', 'class': 'form-control col-sm-8', 'placeholder': 'Напишите свой логин'}))
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'style': 'margin:10px; padding:10px; height:40px', 'class': 'form-control col-sm-8', 'placeholder': 'Введите пароль не мение 5 символов'}))



class FeedbackForm(forms.Form):
    # name = forms.CharField(label='Имя', max_length=100)
    # email = forms.EmailField(label='Почта')
    # phone = forms.CharField(label='Телефон', max_length=100)
    # message = forms.TextField(label='Сообщение')

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'phone', 'message')


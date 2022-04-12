from django import forms
from starline.models import Comment, Feedback


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'name', 'numbers_phone', 'body')
        widgets = {'numbers_phone': forms.TextInput(attrs={
            'type': 'tel',
            'placeholder': '+375 (__)___-__-__',
            'value': '+375'
        })}


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(label='ФИО', widget=forms.TextInput(attrs={'placeholder': 'Иванов Иван Иванович'}))
    phone = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={
        'type': 'tel',
        'placeholder': '+375 (__)___-__-__',
        'value': '+375'}))
    message = forms.CharField(label='Опишите свой вопрос', widget=forms.Textarea(
        attrs={'placeholder': 'Хочу установить иммобилайзер и не потерять гарантию дилера'}))

    class Meta:
        model = Feedback
        fields = ('name', 'phone', 'message')


class FeedbackFormCon(forms.ModelForm):
    phone_c = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={
        'type': 'tel',
        'placeholder': '+375 (__)___-__-__',
        'value': '+375', 'class': 'main__input'}))

    class Meta:
        model = Feedback
        fields = ('phone_c',)

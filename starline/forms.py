from django import forms
from starline.models import Comment, Feedback, Category, Security


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'name', 'numbers_phone', 'body')
        widgets = {'numbers_phone': forms.TextInput(attrs={'type': 'tel',
                                                           'placeholder': '+375 (__)___-__-__',
                                                           'value': '+375'})}


class FeedbackForm(forms.ModelForm):
    message = forms.CharField(label='Текст письма', widget=forms.Textarea(
        attrs={'style': 'margin:10px; padding:10px; height:200px', 'class': 'form-control col-sm-8',
               'placeholder': 'Напишите марку автомобиля и модель'}))

    class Meta:
        model = Feedback
        fields = ('name', 'phone', 'message')
        widgets = {'phone': forms.TextInput(attrs={'type': 'tel',
                                                   'placeholder': '+375 (__)___-__-__',
                                                   'value': '+375'})}


class ProductFilterForm(forms.Form):
    foo_select = forms.ModelMultipleChoiceField(queryset=Category.objects.filter(published=True), widget=forms.CheckboxSelectMultiple)



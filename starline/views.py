from django.contrib.sites import requests
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from rest_framework import viewsets

from .forms import CommentForm, FeedbackForm
from .models import Comment, Contacts, Category, Product, Feedback, Action, OurWork
from .serialeziers import CommentSerializer, PopularProductSerializer, NoveltiesProductSerializer


#  Добавить токен tele_bot_token и chat_id пользователя, которому будут приходить сообщения (chat_id у @userinfobot)
#  Пользователь, которому будут приходить сообщения должен добавить себе своего бота.
# Telegram bot GLOBAL SETTINGS
tele_bot_token = '5259906909:AAGwzQMWTVFTVuQha9NPOROQjzVGxYCVfys'
chat_id = 821421337


def index(request):
    return render(request, 'starline/index.html')


#  Добавить токен tele_bot_token и chat_id пользователя, которому будут приходить сообщения (chat_id у @userinfobot)
#  Пользователь, которому будут приходить сообщения должен добавить себе своего бота.
# Telegram bot GLOBAL SETTINGS
tele_bot_token = '5259906909:AAGwzQMWTVFTVuQha9NPOROQjzVGxYCVfys'
chat_id = 821421337


def layout(request):
    return render(request, 'layout.html')


class CommentView(CreateView):
    """Создание отзыва"""
    model = Comment
    template_name = 'form_comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('layout')


class СontactsView(ListView):
    """Контакты и информация"""
    model = Contacts
    template_name = 'contacts.html'
    context_object_name = 'contacts'


def phone_form_view(request):
    """Телеграм бот из формы"""
    phone_form = FeedbackForm()
    if request.method == 'POST':
        phone_form = FeedbackForm(request.POST)
        if phone_form.is_valid():
            updated_values = {'published': False}
            phone_number = phone_form.cleaned_data['phone']
            name = phone_form.cleaned_data['name']
            message = phone_form.cleaned_data['message']
            Feedback.objects.update_or_create(phone=phone_number, name=name, message=message, defaults=updated_values)
            response = requests.post(
                url=f'https://api.telegram.org/bot{tele_bot_token}/sendMessage',
                data={'chat_id': chat_id,
                      'text': f'*Поступила новая заявка от:* {phone_number}\n*Имя:* {name}\n*Сообщение:* {message}',
                      'parse_mode': 'markdown'}).json()
            return redirect('layout')
    context = {'phone_form': phone_form}
    return render(request, 'feedback.html', context)


def phone_form_view(request):
    """Телеграм бот из формы"""
    phone_form = FeedbackForm()
    if request.method == 'POST':
        phone_form = FeedbackForm(request.POST)
        if phone_form.is_valid():
            updated_values = {'published': False}
            phone_number = phone_form.cleaned_data['phone']
            name = phone_form.cleaned_data['name']
            message = phone_form.cleaned_data['message']
            Feedback.objects.update_or_create(phone=phone_number, name=name, message=message, defaults=updated_values)
            response = request.post(
                url=f'https://api.telegram.org/bot{tele_bot_token}/sendMessage',
                data={'chat_id': chat_id,
                      'text': f'*Поступила новая заявка от:* {phone_number}\n*Имя:* {name}\n*Сообщение:* {message}',
                      'parse_mode': 'markdown'}).json()
            return redirect('layout')
    context = {'phone_form': phone_form}
    return render(request, 'feedback.html', context)


# @receiver(post_save, sender=Feedback)
# def my_handler(sender, **kwargs):
#     """Отправка сообщений на почту через форму обратной связи"""
#     name = kwargs['instance']
#     mine = Feedback.objects.filter(name=name.name).last()  # Берет с QuerySet последний объект
#     send_mail(
#         subject='Новая заявка',
#         message=f'Заявка от: {mine.name} Номер телефона: {mine.phone} Сообщение: {mine.message}',
#         from_email="Starline",
#         recipient_list=['olegpustovalov220@gmail.com'],  # почтовый ящик(и) куда отправляем письма
#         fail_silently=False,
#     )


class ActionView(ListView):
    """Вывод акций на экран"""
    model = Action
    template_name = 'action.html'
    context_object_name = 'action'

    def get_queryset(self):
        return Action.objects.filter(published=True)


class CatalogView(ListView):
    """Вывод категорий на экран"""
    model = Category
    template_name = 'catalog.html'
    context_object_name = 'category'

    def get_queryset(self):
        queryset = Category.objects.filter(published=True).order_by('id')
        return queryset


class OurWorkView(ListView):
    """Наши работы"""
    model = OurWork
    template_name = 'our_work.html'
    context_object_name = 'our_work'


class AllProductView(ListView):
    """Вывод продуктов на экран"""
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        queryset = Product.objects.filter(category__slug=self.kwargs['cat_slug'], published=True).order_by('id')
        return queryset


class DetailProductView(DetailView):
    """Детализация продукта"""
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'prod'
    slug_url_kwarg = 'prod_slug'


class CommentViewSet(viewsets.ReadOnlyModelViewSet):
    """
        API для отзыва
    """
    queryset = Comment.objects.filter(published=True)
    serializer_class = CommentSerializer


class PopularProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
        API для популярного продукта
    """
    queryset = Product.objects.filter(popular=True)
    serializer_class = PopularProductSerializer


class NoveltiesProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
        API для новинок продукта
    """
    queryset = Product.objects.filter(novelties=True)
    serializer_class = NoveltiesProductSerializer

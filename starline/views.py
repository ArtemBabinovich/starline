from django.db.models import Prefetch
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
import requests  # Не удалять нужен для Telegram bot

from .forms import FeedbackForm, FeedbackFormCon
from .models import Comment, Contacts, Category, Product, Feedback, Action, OurWork, Security, Company
from .serialeziers import CommentSerializer, PopularProductSerializer, NoveltiesProductSerializer, OurWorkSerializer, \
    SecuritySerializer, CategoryWorkSerializer, ProductSerializer, CategorySerializer

#  Добавить токен tele_bot_token и chat_id пользователя, которому будут приходить сообщения (chat_id у @userinfobot)
#  Пользователь, которому будут приходить сообщения должен добавить себе своего бота.
# Telegram bot GLOBAL SETTINGS
tele_bot_token = '5259906909:AAGwzQMWTVFTVuQha9NPOROQjzVGxYCVfys'
chat_id = 821421337


def index(request):
    contacts = Contacts.objects.all()
    products = Product.objects.count()
    """Телеграм бот из формы для заявки"""
    phone_form = FeedbackForm()
    if request.method == 'POST':
        phone_form = FeedbackForm(request.POST)
        if phone_form.is_valid():
            updated_values = {'published': False}
            phone_number = phone_form.cleaned_data['phone']
            name = phone_form.cleaned_data['name']
            message = phone_form.cleaned_data['message']
            Feedback.objects.update_or_create(phone=phone_number, name=name, message=message, defaults=updated_values)
            requests.post(
                url=f'https://api.telegram.org/bot{tele_bot_token}/sendMessage',
                data={'chat_id': chat_id,
                      'text': f'*Новая заявка:* {phone_number}\n*Имя:* {name}\n*Сообщение:* {message}',
                      'parse_mode': 'markdown'}).json()
            return render(request, template_name='starline/index.html')

    """Телеграм бот из формы для консультации"""
    phone_con = FeedbackFormCon()
    if request.method == 'POST':
        phone_con = FeedbackFormCon(request.POST)
        if phone_con.is_valid():
            updated_values = {'published': False}
            phone_number = phone_con.cleaned_data['phone_c']
            Feedback.objects.update_or_create(phone=phone_number, defaults=updated_values)
            requests.post(
                url=f'https://api.telegram.org/bot{tele_bot_token}/sendMessage',
                data={'chat_id': chat_id,
                      'text': f'* Нужна консультация:* {phone_number}',
                      'parse_mode': 'markdown'}).json()
            return render(request, template_name='starline/index.html')
    context = {
        'products': products,
        'contacts': contacts,
        'phone_form': phone_form,
        'phone_con': phone_con,
    }
    return render(request, 'starline/index.html', context=context)


class ContactsView(ListView):
    """Контакты и информация"""
    model = Contacts
    template_name = 'starline/contact.html'
    context_object_name = 'contacts'


class AboutCompanyView(ListView):
    """О компании"""
    model = Company
    template_name = 'starline/about_company.html'
    context_object_name = 'company'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contacts.objects.all()
        return context


class ActionView(ListView):
    """Вывод акций на экран"""
    model = Action
    template_name = 'starline/action.html'
    context_object_name = 'action'

    def get_queryset(self):
        return Action.objects.filter(published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contacts.objects.all()
        return context


class CatalogView(ListView):
    """Вывод категорий на экран"""
    model = Category
    template_name = 'catalog.html'
    context_object_name = 'category'

    def get_queryset(self):
        queryset = Category.objects.filter(published=True).order_by('id')
        return queryset


def listourwork(request):
    """наши работы"""
    contacts = Contacts.objects.all()
    context = {'contacts': contacts}
    return render(request, 'starline/portfolio_all.html', context)


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
    template_name = 'starline/product_page.html'
    context_object_name = 'prod'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contacts.objects.all()
        return context


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


class OurWorkViewSet(viewsets.ReadOnlyModelViewSet):
    """
        API для наши работы
    """
    queryset = OurWork.objects.filter(published=True)
    serializer_class = OurWorkSerializer


class CategotyFiltViewSet(viewsets.ReadOnlyModelViewSet):
    """API для создания каталога"""
    queryset = Security.objects.prefetch_related(
        Prefetch(
            'categores',
            queryset=Category.objects.filter(published=True)
        )
    )
    serializer_class = SecuritySerializer


class CategoryWorkViewSet(viewsets.ReadOnlyModelViewSet):
    """Наши работы по категориям"""
    queryset = Category.objects.filter(published=True).prefetch_related(
        Prefetch(
            'category_work',
            queryset=OurWork.objects.filter(published=True)
        )
    )
    serializer_class = CategoryWorkSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(published=True)
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.filter(published=True)
    serializer_class = CategorySerializer

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from .forms import CommentForm, FeedbackForm
from .models import Comment, Contacts, Category, Product, Feedback


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


class FeedbackView(CreateView):
    """Обратная связь"""
    model = Feedback
    template_name = 'feedback.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('layout')


@receiver(post_save, sender=Feedback)
def my_handler(sender, **kwargs):
    name = kwargs['instance']
    mine = Feedback.objects.filter(name=name.name).last()  # Берет с QuerySet последний объект
    send_mail(
        subject='Новая заявка',
        message=f'Новая заявка {mine.name} Номер телефона: {mine.phone} Сообщение: {mine.message} Email: {mine.email}',
        from_email="Starline",
        recipient_list=[''],  # почтовый ящик(и) куда отправляем письма
        fail_silently=False,
    )


class CatalogView(ListView):
    """Вывод категорий на экран"""
    model = Category
    template_name = 'catalog.html'
    context_object_name = 'category'

    def get_queryset(self):
        queryset = Category.objects.filter(published=True).order_by('id')
        return queryset


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

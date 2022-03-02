from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from .forms import CommentForm
from .models import Comment, Contacts, Feedback, Category, Product


def layout(request):
    return render(request, 'layout.html')


class CommentView(CreateView):
    """Создание отзыва"""
    model = Comment
    template_name = 'form_comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('layout')


def contact(request):
    contacts = Contacts.objects.all()
    context = {
        'contacts': contacts,
    }
    return render(request, template_name='contacts.html', context=context)


def feedb(request):
    feedback = Feedback.objects.all()
    context = {
        'feedback': feedback,
    }
    return render(request, template_name='feedback.html', context=context)


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
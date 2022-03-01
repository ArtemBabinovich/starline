from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from starline.forms import CommentForm
from starline.models import Comment
from django.template import context
from django.views.generic import ListView
from starline.models import Contacts, Feedback

def index(request):
    return render(request, 'index.html')


class CommentView(CreateView):
    """Создание отзыва"""
    model = Comment
    template_name = 'form_comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('index')


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

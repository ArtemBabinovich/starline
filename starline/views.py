from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from starline.forms import CommentForm
from starline.models import Comment


def index(request):
    return render(request, 'index.html')


class CommentView(CreateView):
    """Создание отзыва"""
    model = Comment
    template_name = 'form_comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('index')

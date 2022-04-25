from django.db.models import Prefetch
from rest_framework import viewsets
from .models import Comment, Product, OurWork, Security, Category, Characteristic
from .serialeziers import CommentSerializer, PopularProductSerializer, NoveltiesProductSerializer, OurWorkSerializer, \
    SecuritySerializer, ProductSerializer, CategorySerializer, CharacteristicSerializer


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


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """API все продукты"""
    queryset = Product.objects.filter(published=True).prefetch_related(
        Prefetch(
            'characteristics',
            queryset=Characteristic.objects.all()
        )
    )
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """API всех категорий"""
    queryset = Category.objects.filter(published=True)
    serializer_class = CategorySerializer


class CharacteristicSerializerViewSet(viewsets.ReadOnlyModelViewSet):
    """API всех функций"""
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer

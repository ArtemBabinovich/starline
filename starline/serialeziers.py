from rest_framework import serializers

from starline.models import Security, Category, Characteristic, Product, Comment


class SecuritySerializer(serializers.ModelSerializer):
    """Охранные комплексы"""
    categores = serializers.StringRelatedField(many=True)

    class Meta:
        model = Security
        fields = ['title', 'categores']
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    """Категории комплексов"""
    class Meta:
        model = Category
        fields = ['title', ]
        depth = 1


class CharacteristicSerializer(serializers.ModelSerializer):
    """Характеристика"""

    class Meta:
        model = Characteristic
        fields = ['title', 'description']
        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    """Товар"""
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'price_install',
            'image',
            'category',
            'presence',
            'instruction',
            'popular',
            'novelties',
        ]
        depth = 1


class CommentSerializer(serializers.ModelSerializer):
    """Отзыв на работу"""
    class Meta:
        model = Comment
        fields = ['title', 'name', 'body']

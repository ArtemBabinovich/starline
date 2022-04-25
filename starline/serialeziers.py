from rest_framework import serializers

from starline.models import Security, Category, Characteristic, Product, Comment, OurWork


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


class CharacteristicSerializer(serializers.ModelSerializer):
    """Характеристика"""

    class Meta:
        model = Characteristic
        fields = ['title', ]
        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    characteristics = serializers.StringRelatedField(many=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'slug',
            'price',
            'price_install',
            'image',
            'presence',
            'instruction',
            'characteristics',
            'category',
        ]
        depth = 1


class PopularProductSerializer(serializers.ModelSerializer):
    """Популярный Товар"""
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'slug',
            'price',
            'price_install',
            'image',
            'category',
            'presence',
            'instruction',
        ]
        depth = 1


class NoveltiesProductSerializer(serializers.ModelSerializer):
    """Новинка Товара"""
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'slug',
            'price',
            'price_install',
            'image',
            'category',
            'presence',
            'instruction',
        ]
        depth = 1


class CommentSerializer(serializers.ModelSerializer):
    """Отзыв на работу"""
    class Meta:
        model = Comment
        fields = ['title', 'name', 'body']


class OurWorkSerializer(serializers.ModelSerializer):
    """Наши работы"""
    category_work = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = OurWork
        fields = [
            'title',
            'slug',
            'installation_time',
            'installation_price',
            'category_work',
            'image1',

        ]
        depth = 1

import re

from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone
from slugify import slugify


class Security(models.Model):
    """Охранные комплексы"""
    title = models.CharField('Название комплекса', max_length=250)

    class Meta:
        verbose_name = 'Комплекс'
        verbose_name_plural = 'Комплексы'
        ordering = ('-id',)

    def __str__(self):
        return self.title


class Category(models.Model):
    """Категории комплексов"""
    title = models.CharField('Название категории комплекса', max_length=250)
    slug = models.SlugField('Короткое название', unique=True, db_index=True, max_length=20, blank=True, null=True)
    security = models.ForeignKey(Security, related_name='categores', on_delete=models.CASCADE, verbose_name='Название комплекса')
    published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-id',)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title))
        return super().save(*args, **kwargs)


class Characteristic(models.Model):
    """Характеристика"""
    title = models.CharField('Название характеристики', max_length=250)
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return self.title


class Product(models.Model):
    """Товар"""
    PRESENCE_CHOICES = [
        ["Есть в наличии", "Есть в наличии"],
        ["Под заказ", "Под заказ"],
        ["Нет в наличии", "Нет в наличии"]
    ]
    title = models.CharField('Название товара', max_length=250)
    slug = models.CharField('Короткое название', max_length=20, unique=True, db_index=True, blank=True, null=True)
    description = RichTextUploadingField('Описание')
    price = models.DecimalField('Цена оборудования', decimal_places=2, max_digits=7, blank=True, null=True)
    price_install = models.DecimalField('Цена установки', decimal_places=2, max_digits=7, blank=True, null=True)
    image = models.ImageField('Картинка', blank=True, null=True, upload_to='image/%Y/%m/%d/')
    category = models.ManyToManyField(Category, related_name='cat', verbose_name='Категория')
    presence = models.CharField('Наличие товара', max_length=200, choices=PRESENCE_CHOICES)
    characteristics = models.ManyToManyField(
        Characteristic,
        related_name='charecter',
        blank=True,
        null=True,
        verbose_name='Характеристики'
    )
    instruction = models.FileField('Инструкция', upload_to='file_instruction/%Y/%m/%d/', blank=True, null=True)
    published = models.BooleanField('Опубликовано', default=True)
    popular = models.BooleanField('Популярный товар', default=False)
    novelties = models.BooleanField('Новинка', default=False)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('-id',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title))
        return super().save(*args, **kwargs)


class Action(models.Model):
    """Акции и скидки"""
    title = models.CharField('Название акции', max_length=250)
    description = RichTextUploadingField('Описание акции')
    image = RichTextUploadingField('Изображение', blank=True, null=True, config_name='customimage')
    published = models.BooleanField('Опубликовано', default=False)

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.title


def validate_phone(value):
    validation_expression = r'^\+375\(\d{2}\)\d{3}-\d{2}-\d{2}$'
    if not re.match(validation_expression, value):
        raise ValidationError(
            _('Номер телефона должен быть в формате +375(XX)XXX-XX-XX'),
            code='invalid_phone_format'
        )


class Comment(models.Model):
    """Отзыв на работу"""
    title = models.CharField('Заголовок отзыва', max_length=200)
    name = models.CharField('Имя отправителя отзыва', max_length=200, db_index=True)
    numbers_phone = models.CharField('Номер телефона', max_length=17, validators=[validate_phone])
    body = models.TextField('Содержимое комментария')
    pub_data = models.DateTimeField('Дата комментария', default=timezone.now)
    published = models.BooleanField('Опубликовано', default=False)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('pub_data',)

    def __str__(self):
        return f'Отзыв от {self.name} с текстом: {self.body[:20]}'


class OurWork(models.Model):
    """Наши работы"""
    title = models.CharField('Заголовок', max_length=250)
    category_work = models.ManyToManyField(
        Category,
        related_name='category_work',
        verbose_name='категория установленного оборудования',
    )
    installation_time = models.CharField('Время установки', max_length=100)
    installation_price = models.CharField('Стоимость установки', max_length=100)
    description_video = RichTextUploadingField('Описание видео', blank=True, null=True)
    url = models.TextField('Видео', help_text='Вставить ссылку с YouTube', blank=True, null=True)
    description_image = RichTextUploadingField('Описание фото', blank=True, null=True)
    image = RichTextUploadingField('Изображение', blank=True, null=True, config_name='customimage')
    published = models.BooleanField('Опубликовано', default=False)

    class Meta:
        verbose_name = 'Наши работы'
        verbose_name_plural = 'Наша работа'

    def __str__(self):
        return self.title


class Feedback(models.Model):
    """Обратная связь"""
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=50, validators=[validate_phone])
    message = models.TextField('Сообщение', blank=True, null=True)
    published = models.BooleanField('Обработано', default=False)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return f'{self.name} : {self.message}'


class Contacts(models.Model):
    """Контакты и информация"""
    name = models.CharField('Название сервиса', max_length=200, blank=True, null=True)
    address = models.CharField('Адрес сервиса', max_length=250)
    logo1 = models.ImageField(
        'Логотип оператора связи 1',
        blank=True,
        null=True,
        upload_to='image/logo_phone/%Y/%m/%d/',
    )
    phone1 = models.CharField('Номер телефона сервиса 1', max_length=50, blank=True, null=True)
    logo2 = models.ImageField(
        'Логотип оператора связи 2',
        blank=True,
        null=True,
        upload_to='image/logo_phone/%Y/%m/%d/',
    )
    phone2 = models.CharField('Номер телефона сервиса 2', max_length=50, blank=True, null=True)
    email = models.CharField('Электронная почта', max_length=200, blank=True, null=True)
    social_info1 = models.CharField('Социальная сеть 1', max_length=200, blank=True, null=True)
    social_info2 = models.CharField('Социальная сеть 2', max_length=200, blank=True, null=True)
    social_info3 = models.CharField('Социальная сеть 3', max_length=200, blank=True, null=True)
    time_work1 = models.CharField('Время работы (будни)', max_length=100, blank=True, null=True)
    time_work2 = models.CharField('Время работы (выходные)', max_length=100, blank=True, null=True)
    maps = models.TextField(
        'Расположение на карте',
        help_text='Вставить скрипт или ссылку с конструктора карт',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.address


class Company(models.Model):
    image = models.ImageField('Картинка', blank=True, null=True, upload_to='image/%Y/%m/%d/')
    description = RichTextUploadingField('Описание', blank=True, null=True)
    published = models.BooleanField('Опубликовано', default=False)

    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'

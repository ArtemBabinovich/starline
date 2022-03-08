import re

from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone
from slugify import slugify


class NumberPhone(models.Model):
    """Номер и логотип для обратной связи"""
    logo = models.ImageField('Логотип оператора связи')
    numbers = models.CharField('Номер телефона', max_length=50)

    def __str__(self):
        return f'{self.numbers}'

    class Meta:
        verbose_name = 'Моб.номер'
        verbose_name_plural = 'Моб.номера'


class OurWorks(models.Model):
    """Фотографии и видео работ"""
    picture = models.ImageField('Фотографии работ')
    video_url = models.CharField('Видео работ', max_length=250)


class Warranty_Support(models.Model):
    """Гарантия и поддержка"""
    description = models.TextField('Гарантия и поддержка')

    class Meta:
        verbose_name = 'Гарантия'
        verbose_name_plural = 'Гарантии'

    def __str__(self):
        return self.description


class Security(models.Model):
    """Охранные комплексы"""
    title = models.CharField('Название ', max_length=100)


class Category(models.Model):
    """Категории комплексов"""
    title = models.CharField('Название категории', max_length=100)
    slug = models.SlugField('Слаг', unique=True, db_index=True, max_length=20, blank=True, null=True)
    published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-id',)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title))
        return super().save(*args, **kwargs)


class Product(models.Model):
    """Продукт"""
    title = models.CharField('Название', max_length=200)
    slug = models.CharField('Слаг', max_length=20, unique=True, db_index=True, blank=True, null=True)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена без установки', decimal_places=2, max_digits=7, blank=True, null=True)
    price_install = models.DecimalField('Цена с установкой', decimal_places=2, max_digits=7, blank=True, null=True)
    time_first = models.CharField('Время установки 1', max_length=10, blank=True, null=True)
    time_second = models.CharField('Время установки 2', max_length=10, blank=True, null=True)
    image = models.ImageField('Картинка', blank=True, null=True, upload_to="image/%Y/%m/%d/")
    category = models.ManyToManyField(Category, related_name='cat', verbose_name='Категория')
    published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('-id',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title))
        return super().save(*args, **kwargs)


def validate_phone(value):
    validation_expression = r'^\+375\(\d{2}\)\d{3}-\d{2}-\d{2}$'
    if not re.match(validation_expression, value):
        raise ValidationError(
            _('Номер телефона должен быть в формате +375(XX)XXX-XX-XX'),
            code='invalid_phone_format'
        )


class Comment(models.Model):
    """Отзыв на работу"""
    name = models.CharField('Имя отправителя отзыва', max_length=200, db_index=True)
    numbers_phone = models.CharField('Номер телефона', max_length=17, validators=[validate_phone])
    body = models.TextField('Содержимое комментария')
    pub_data = models.DateTimeField('Дата комментария', default=timezone.now)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('pub_data',)

    def __str__(self):
        return f'Отзыв от {self.name} с текстом: {self.body}'


class Answer_Comment(models.Model):
    """Ответ на отзыв"""
    name = models.CharField('Имя', max_length=250)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='Содержимое отзыва')
    body = models.TextField('Ответ на отзыв')
    pub_data = models.DateTimeField('Дата ответа на комментарий', default=timezone.now)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы на отзывы'

    def __str__(self):
        return f'Ответ от {self.name} с текстом: {self.body}'


class Contacts(models.Model):
    """Контакты и информация"""
    name = models.CharField('Название магазина', max_length=100)
    address = models.CharField('Адрес магазина', max_length=100)
    phone1 = models.CharField('Номер телефона 1', max_length=50, blank=True, null=True)
    phone2 = models.CharField('Номер телефона 2', max_length=50, blank=True, null=True)
    phone_service = models.CharField('Номер телефона сервиса', max_length=50, blank=True, null=True)
    email = models.CharField('Электронная почта', max_length=100)
    social_info = models.CharField('Социальная сеть', max_length=100, blank=True, null=True)
    time_work1 = models.CharField('Время работы (будни)', max_length=100, blank=True, null=True)
    time_work2 = models.CharField('Время работы (выходные)', max_length=100, blank=True, null=True)
    maps = models.TextField('Расположение на карте', help_text='Вставить скрипт или ссылку с конструктора карт', blank=True, null=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.address


class Feedback(models.Model):
    """Обратная связь"""
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=50, validators=[validate_phone])
    message = models.TextField('Сообщение')
    published = models.BooleanField('Обработано', default=False)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return self.message


class Action(models.Model):
    """Акции"""
    title = models.CharField('Название акции', max_length=100)
    description = RichTextUploadingField('Описание акции')
    date = models.DateField('Дата добавления')
    published = models.BooleanField('Опубликовано')

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.title


class Our_work(models.Model):
    """Наши работы"""
    description_video = RichTextUploadingField('Описание видео', blank=True)
    url = models.TextField('Видео', help_text='Вставить ссылку с YouTube', blank=True)
    description_image = RichTextUploadingField('Описание фото', blank=True)
    image = RichTextUploadingField('Изображение', blank=True, null=True, config_name='customimage')
    date = models.DateField('Дата добавления')

    class Meta:
        verbose_name = 'Наши работы'
        verbose_name_plural = 'Наша работа'

    def __str__(self):
        return self.description_video


class Service(models.Model):
    """Сервис"""
    title = models.CharField('Название услуги', max_length=100)
    description = models.TextField('Описание услуги')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    published = models.BooleanField('Опубликовано')

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service', kwargs={'slug': self.slug})





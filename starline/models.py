import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone


class NumberPhone(models.Model):
    """Номер и логотип для обратной связи"""
    logo = models.ImageField('Логотип оператора связи')
    numbers = models.CharField('Номер телефона', max_length=50)

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

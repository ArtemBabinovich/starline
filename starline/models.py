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


class Comment(models.Model):
    """Отзыв на работу"""
    name = models.CharField('Имя отправителя отзыва', max_length=200, db_index=True)
    numbers_phone = models.CharField('Номер телефона', max_length=50)
    body = models.TextField('Содержимое комментария')
    pub_data = models.DateTimeField('Дата комментария', default=timezone.now)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('pub_data',)

    def __str__(self):
        return f'Отзыв от {self.name} с текстом: {self.body}'

from django.db import models


class NumberPhone(models.Model):
    """Номер и логотип для обратной связи"""
    logo = models.ImageField('Логотип оператора связи')
    numbers = models.CharField('Номер телефона', max_length=50)

    def __str__(self):
        return f'{numbers}'
      
    class Meta:
        verbose_name = 'Моб.номер'
        verbose_name_plural = 'Моб.номера'


class OurWorks(models.Model):
    """Фотографии и видео работ"""
    picture = models.ImageField('Фотографии работ')
    video_url = models.CharField('Видео работ', max_length=200)


class Warranty_Support(models.Model):
    """Гарантия и поддержка"""
    description = models.TextField('Гарантия и поддержка')

    class Meta:
        verbose_name = 'Гарантия'
        verbose_name_plural = 'Гарантии'

    def __str__(self):
        return self.description

from django.db import models


class NumberPhone(models.Model):
    """Номер и логотип для обратной связи"""
    logo = models.ImageField('Логотип оператора связи')
    numbers = models.CharField('Номер телефона', max_length=50)


class OurWorks(models.Model):
    """Фотографии и видео работ"""
    picture = models.ImageField('Фотографии работ')
    video_url = models.CharField('Видео работ')


class Warranty_Support(models.Model):
    """Гарантия и поддержка"""
    description = models.TextField('Гарантия и поддержка')

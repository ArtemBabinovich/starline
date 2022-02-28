from django.db import models


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
    video_url = models.CharField('Видео работ', max_length=200)


class Warranty_Support(models.Model):
    """Гарантия и поддержка"""
    description = models.TextField('Гарантия и поддержка')

    class Meta:
        verbose_name = 'Гарантия'
        verbose_name_plural = 'Гарантии'

    def __str__(self):
        return self.description


class Contacts(models.Model):
    """Контакты и информация"""
    name = models.CharField('Название магазина', max_length=100)
    address = models.CharField('Адрес магазина', max_length=100)
    phone1 = models.CharField('Номер телефона1', max_length=50, blank=True, null=True)
    phone2 = models.CharField('Номер телефона2', max_length=50, blank=True, null=True)
    phone_service = models.CharField('Номер телефона сервиса', max_length=50, blank=True, null=True)
    email = models.CharField('Электронная почта', max_length=100)
    social_info = models.CharField('Социальная сеть', max_length=100, blank=True, null=True)
    time_work1 = models.CharField('Время работы (будни)', max_length=100, blank=True, null=True)
    time_work2 = models.CharField('Время работы (выходные)', max_length=100, blank=True, null=True)
    maps = models.TextField('Расположение на карте', blank=True, null=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.address


class Feedback(models.Model):
    """Обратная связь"""
    name = models.CharField('Имя', max_length=100)
    email = models.CharField('E-mail', max_length=100, blank=True)
    phone = models.CharField('Телефон', max_length=50)
    message = models.TextField('Сообщение')
    published = models.BooleanField('Обработано', default=True)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return f'Письмо от {self.name}. Телефон: {self.phone}. Сообщение: {self.message}. '

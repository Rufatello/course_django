from django.db import models


class Client(models.Model):
    Email = models.EmailField(verbose_name='Почта',max_length=254, unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=100)
    last_name = models.CharField(verbose_name='Фамилия', max_length=100)
    surname = models.CharField(verbose_name='Отчетсво', max_length=100)
    comment = models.TextField(verbose_name='Комментарий', null=True, blank=True)
    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.surname}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'



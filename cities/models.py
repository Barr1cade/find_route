from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Город')
    station = models.CharField(max_length=100, verbose_name='Вокзал')
    platform = models.CharField(max_length=10, verbose_name='Путь номер')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('trains:detail', kwargs={'pk': self.pk})

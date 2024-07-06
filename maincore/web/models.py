from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class SimpleModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование Сырья')
    iron_content = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name='Содержание железа')
    si_content = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name='Содержание кремния')
    al_content = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name='Содержание алюминия')
    ca_content = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name='Содержание кальция')
    sulfur_content = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name='Содержание серы')
    create_time = models.DateField(default=timezone.now, verbose_name='Время добавления')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

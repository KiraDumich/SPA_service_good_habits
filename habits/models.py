from datetime import timedelta

from django.db import models
from users.models import User

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Владелец', **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='Место')
    time = models.DateTimeField(auto_now=True, verbose_name='Время когда выполняется привычка')
    action = models.CharField(max_length=150, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Связанная привычка', **NULLABLE)
    period = models.PositiveSmallIntegerField(default=1, verbose_name='Периодичность в днях')
    reward = models.CharField(max_length=150, verbose_name='Вознаграждение')
    duration = models.DurationField(default=timedelta(minutes=2), verbose_name='Время на выполнение (минуты)')
    is_public = models.BooleanField(default=False, verbose_name='Публичная')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

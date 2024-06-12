import os
from celery import shared_task
from datetime import timedelta

from django.utils import timezone

from habits.models import Habit
from habits.services import send_message


@shared_task
def send_notification():  # Функция отправки уведомления
    time_now = timezone.now()
    habits = Habit.objects.all()
    token = os.getenv('TOKEN_BOT')

    for habit in habits:
        if habit.time >= time_now - timedelta(minutes=15):
            message = f"Не забудь про привычку '{habit.action}'\n" \
                      f"После этого можно:\n \
{habit.related_habit if habit.related_habit else habit.reward}"
            send_message(token=token,
                         chat_id=habit.owner.chat_id,
                         message=message)

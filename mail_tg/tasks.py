import datetime

from celery import shared_task
from django.utils import timezone

from habit.models import HabitGood, HabitNice
from mail_tg.services import TGBot


@shared_task
def mail_tg_reminder():
    mail_list = HabitGood.objects.filter(time__lt=timezone.now() - timezone.timedelta(minutes=1))
    if len(mail_list) > 0:
        bot = TGBot()
        for mail in mail_list:
            if mail.reward:
                reward = mail.reward
            elif mail.connect_habit_id:
                habit_nice = HabitNice.objects.filter(id=mail.connect_habit_id).first()
                reward = habit_nice.action
            else:
                reward = "ничего"
            text = f'Я должен {mail.action} в {mail.time} {mail.place}. В награду будет {reward}'
            print(text)
            bot.send_message(text=text)

from django.db import models
from backend.models.Text import Language

class TelegramUser(models.Model):
    telegram_id = models.CharField(max_length=32, verbose_name="Телеграм ID")
    full_name = models.CharField(max_length=128, verbose_name="Пользователь")
    selected_language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)


from django.db import models
from datetime import datetime

# Create your models here.

# dinh nghia cau truc va cac truong du lieu cho cac tin nhan cua phong chat, moi tin nhan, 
# phong chat duoc luu duoi dang mot doi tuong Message, Room trong CSDL
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
from django.contrib import admin
from .models import Room, Message

# Register your models here.

# dang ky mo hinh Room va Message voi giao dien admin
admin.site.register(Room)
admin.site.register(Message)
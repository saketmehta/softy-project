from django.contrib import admin
from .models import Message, Question

# Register your models here.

admin.site.register(Question)
admin.site.register(Message)
from django.contrib import admin
from .models import Profile, Student, Tutor, Message, Question

# Register your models here.

admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(Message)
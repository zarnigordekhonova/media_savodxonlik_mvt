from django.contrib import admin
from .models import Lesson, LessonProgress
# Register your models here.

admin.site.register(Lesson)
admin.site.register(LessonProgress)
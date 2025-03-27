from django.urls import path
from .views import lesson_list, lesson_detail, mark_watched

app_name = 'lessons'
urlpatterns = [
    path('lessons/', lesson_list, name='lesson_list'),
    path('lessons/<int:lesson_id>/', lesson_detail, name='lesson_detail'),
    path('lessons/<int:lesson_id>/watched/', mark_watched, name='mark_watched'),
]

from django.db import models
from django.conf import settings


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='Lessons/')
    test_url = models.URLField()

    def __str__(self):
        return self.title


class LessonProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'lesson')

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title} - {'Watched' if self.watched else 'Not Watched'}"

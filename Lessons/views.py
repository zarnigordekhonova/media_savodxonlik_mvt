from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Lesson, LessonProgress


@login_required
def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'Lessons/lesson_list.html', {'lessons': lessons})


@login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    progress, created = LessonProgress.objects.get_or_create(user=request.user, lesson=lesson)

    return render(request, 'Lessons/lesson_detail.html', {'lesson': lesson, 'progress': progress})


@login_required
def mark_watched(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    progress, created = LessonProgress.objects.get_or_create(user=request.user, lesson=lesson)

    if request.method == 'POST':
        progress.watched = True
        progress.save()
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})




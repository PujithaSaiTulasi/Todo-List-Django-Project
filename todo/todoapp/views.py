from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def get_todos(request):
    yet_to_do_tasks = TodoList.objects.filter(is_completed=False)
    completed_tasks = TodoList.objects.filter(is_completed=True)
    context = {
        'yet_to_do_tasks': yet_to_do_tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'index.html', context)

@require_http_methods(["POST"])
def create_task(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    date = request.POST.get('date')
    TodoList.objects.create(title=title, description=description, date=date, is_completed=False)
    return redirect('get_todos')

@require_http_methods(["POST"])
def update_task(request, task_id):
    task = get_object_or_404(TodoList, id=task_id)
    task.title = request.POST.get('title')
    task.description = request.POST.get('description')
    task.date = request.POST.get('date')
    task.save()
    return redirect('get_todos')

@require_http_methods(["POST"])
def delete_task(request, task_id):
    task = get_object_or_404(TodoList, id=task_id)
    task.delete()
    return redirect('get_todos')


@require_http_methods(["POST"])
def mark_task_completed(request, task_id):
    task = get_object_or_404(TodoList, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('get_todos')

from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from .models import Task
from .forms import TaskForm


@login_required
def task_list(request, tenant):
    user = request.user
    if user.is_superuser:
        tasks = Task.objects.all().order_by('-due_date')
    else:
        tasks = Task.objects.filter(assigned_to=user).order_by('-due_date')

    paginator = Paginator(tasks, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tracker/task_list.html', {'page_obj': page_obj, 'tenant': tenant})


@login_required
def create_task(request, tenant):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()

            subject = f"New Task Created: {task.title}"
            message = f"""Hi {task.assigned_to.username},

You have been assigned a new task by {request.user.username}

Title: {task.title}
Description: {task.description}
Due Date: {task.due_date}

Login to your dashboard to manage the task.

- Task Manager
"""

            send_mail(
                subject,
                message,
                'arjavbadjate1404@gmail.com',  # Replace with a valid sender
                [task.assigned_to.email],
                fail_silently=False,
            )

            return redirect('tracker:task_list')
    else:
        form = TaskForm()

    return render(request, 'tracker/create_task.html', {'form': form, 'tenant': tenant})


def logout_view(request, tenant):
    logout(request)
    return redirect('tracker:login')


def login_view(request, tenant):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tracker:task_list')
        else:
            return render(request, 'tracker/login.html', {'error': 'Invalid credentials'})
    return render(request, 'tracker/login.html')


@login_required
def delete_task(request, tenant, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tracker:task_list', tenant=tenant)

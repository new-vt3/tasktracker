from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('<str:tenant>/', views.task_list, name='task_list'),
    path('<str:tenant>/create/', views.create_task, name='create_task'),
    path('<str:tenant>/login/', views.login_view, name='login'),
    path('<str:tenant>/logout/', views.logout_view, name='logout'),
    path('<str:tenant>/delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
]
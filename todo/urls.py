from django.urls import path
from todo import views

app_name = 'todo'
urlpatterns = [
    path('', views.home, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    # api
    path('api/all-task', views.get_all_task),
    path('api/task-details', views.task_details),
]
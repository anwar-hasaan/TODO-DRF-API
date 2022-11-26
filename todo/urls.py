from django.urls import path, include
from todo import views

apis_urls = [
    path('welcome', views.welcome),
    path('create-task', views.task_create),
    path('all-task', views.get_all_task),
    path('task-details', views.task_details),
]

app_name = 'todo'
urlpatterns = [
    path('', views.home, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('resfresh-user-uid/<uid>', views.resfresh_user_uid),
    path('api/', include(apis_urls)),
    
]


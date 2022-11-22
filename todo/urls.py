from django.urls import path
from todo import views

app_name = 'todo'
urlpatterns = [
    path('', views.home),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]
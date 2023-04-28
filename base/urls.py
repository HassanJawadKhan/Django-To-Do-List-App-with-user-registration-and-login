from django.urls import path
from .views import task_list, task_detail, task_create, task_update, DeleteView, CustomLoginView, RegisterPage 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', task_list.as_view(), name='tasks'),
    path('task/<int:pk>/', task_detail.as_view(), name='task'),
    path('task-create/', task_create.as_view(), name='task-create'),
    path('task-update/<int:pk>/', task_update.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),



]
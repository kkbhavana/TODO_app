from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views
from .views import TaskList, TaskCreate, TaskDelete, TaskDetailView, TaskUpdate, CustomLoginView, RegisterView

urlpatterns = [
    path('send_email/',views.send_test_email,name='send_mail'),
    path('',views.home,name='home'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
    path('tasklist/', TaskList.as_view(), name='task'),
    path('create/',TaskCreate.as_view(),name='task-create'),
    path('update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('delete/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
    path('details/<int:pk>/', TaskDetailView.as_view(), name='task-details'),

]

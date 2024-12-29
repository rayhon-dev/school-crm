from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('list/', views.student_list, name='list'),
    path('create/', views.student_add, name='add'),
    path('detail/<int:pk>/', views.student_detail, name='detail'),
    path('delete/<int:pk>/', views.student_delete, name='delete'),
    path('update/<int:pk>/', views.student_update, name='update'),
]

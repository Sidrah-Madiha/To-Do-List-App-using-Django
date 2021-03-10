from django.urls import path

# from . import views
from .views import list_view, delete_view
app_name = 'todolist'

urlpatterns = [
    path('', list_view, name='list'),
    path('delete_todo/<int:todo_id>', delete_view),
]





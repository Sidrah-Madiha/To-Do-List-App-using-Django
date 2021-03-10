from django.urls import path

# from . import views
from .views import signup
app_name = 'accounts'

urlpatterns = [
    path('', signup, name='home'),
    path('signup/', signup, name='signup'),
    # path('delete_todo/<int:todo_id>', delete_view),
]
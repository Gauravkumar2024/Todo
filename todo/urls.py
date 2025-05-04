
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signup),
    path('login/', user_login),
    path('todo/', todo),
    path('logout/', user_logout, name='logout'),
    path('update/<int:sr_number>/',updateTodo, name='update'),
    path('delete/<int:sr_number>/',deleteTodo, name='delete')

]

from django.urls import path

from .views import *

app_name = 'todos'

urlpatterns = [    
    path('', todo_list),
    path('create/', todo_create),
    path('<id>/', todo_detail), 
    path('<id>/update/', todo_update), 
    path('<id>/delete/', todo_delete),   
]

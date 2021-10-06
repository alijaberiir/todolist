from django.urls import path
# from .views import todoView,addTodoView,deleteTodoView
from .views import listtodo,addtodo,deltodo,uptodo

urlpatterns = [

    path('',listtodo.as_view()),
    path('add/',addtodo.as_view(),name='add'),
    path('del/<int:pk>/',deltodo.as_view(),name='del'),
    path('up/<int:pk>/',uptodo.as_view(),name='up'),
   
   
]

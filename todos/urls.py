from django.urls import path, include
from .views import ListTodo, DetailTodo, CRUDTodo
from rest_framework import routers  

router = routers.SimpleRouter()
router.register(r'todo', CRUDTodo)


urlpatterns = [
    # path('<int:pk>/', DetailTodo.as_view()),
    # path('', ListTodo.as_view()),
    # path('create/', CRUDTodo.as_view()),
    path('', include(router.urls)),
]
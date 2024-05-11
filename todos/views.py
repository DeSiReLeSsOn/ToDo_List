from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer


class ListTodo(generics.ListApiView):
    queryset = Todo.objects.all()
    serializer = TodoSerializer


class  DetailTodo(generics.RetrieveApiView):
    queryset = Todo.objects.all() 
    serializer = TodoSerializer
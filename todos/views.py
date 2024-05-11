from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodosSerializer


class ListTodo(generics.ListApiView):
    queryset = Todo.objects.all()
    serializer = TodosSerializer


class  DetailTodo(generics.RetrieveApiView):
    queryset = Todo.objects.all() 
    serializer = TodosSerializer
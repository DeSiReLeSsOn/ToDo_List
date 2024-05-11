from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class  DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all() 
    serializer_class = TodoSerializer 



class CreateTodo(APIView):

    def get(self, request):
        todo = Todo.objects.all() 
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data)  

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
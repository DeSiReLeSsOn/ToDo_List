from rest_framework import serializers
from .models import Todo 


class TodosSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Todo 
        firelds = ('id', 'title', 'body',)
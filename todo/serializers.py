from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['uid', 'user_id', 'dev_ref', 'task', 'description', 'status', 'due_date']
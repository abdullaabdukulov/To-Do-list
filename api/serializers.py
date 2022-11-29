from rest_framework import serializers
from .models import Todo


class TODOSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ['user']



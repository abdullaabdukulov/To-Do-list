from rest_framework.viewsets import ModelViewSet
from .models import Todo
from .serializers import TODOSerializer


class TODOViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TODOSerializer


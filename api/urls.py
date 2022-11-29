from rest_framework import routers
from .views import TODOViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'todo', TODOViewSet)

urlpatterns = [
    path('', include(router.urls))
]
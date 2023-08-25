from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DataModelViewSet

router = DefaultRouter()
router.register(r'data-models', DataModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

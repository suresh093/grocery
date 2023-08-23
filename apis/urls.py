from django.urls import path

from .views import CategoryViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories'),
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = router.urls
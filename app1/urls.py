from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet,ProductReviewViewSet

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register('products',ProductViewSet,basename='product')
router.register('reviews',ProductReviewViewSet,basename='product-review')

urlpatterns = [
    path('',include(router.urls)),
    # path('api_auth/',include("rest_framework.urls")),
]

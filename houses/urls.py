from django.urls import path
from django.urls import include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('house', views.HouseViewSet)
router.register('comment', views.CommentViewSet)

urlpatterns = [
    path("", include(router.urls))
    
]
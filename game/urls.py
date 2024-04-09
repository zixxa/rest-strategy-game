from django.urls import path
from rest_framework.routers import DefaultRouter
from game.views import GameViewSet

router = DefaultRouter()

urlpatterns = [
    path("", GameViewSet.as_view({"get":"list"}))
]

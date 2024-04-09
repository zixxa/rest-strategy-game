from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from game.models import Army
from game.serializers import ArmySerializer


class GameViewSet(ModelViewSet):
    serializer_class = ArmySerializer

    def list(self, request, *args, **kwargs):
        queryset = Army.objects.filter(user=self.request.user)
        return Response(data=queryset)

    @action(methods="post", detail=False)
    def charge_army(self):
        pass
from rest_framework import serializers
from game.models import Army


class ArmySerializer(serializers.ModelSerializer):
    class Meta:
        model = Army
        fields = ("name", "score", "currency")

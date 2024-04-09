from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "profile"


class UnitType(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    damage = models.CharField(max_length=20, blank=False, null=False)

    class Meta:
        db_table = "unit_type"


class Army(models.Model):
    unit = models.ForeignKey(Profile, on_delete=models.CASCADE)
    type = models.ForeignKey(UnitType, on_delete=models.CASCADE)
    count = models.IntegerField(blank=False, null=False)

    class Meta:
        db_table = "army"

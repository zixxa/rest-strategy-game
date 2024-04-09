from django.contrib import admin
from django.contrib.admin import ModelAdmin, register

from game.models import Profile, Army


@register(Profile)
class ProfileAdmin(ModelAdmin):
    model = Profile

@register(Army)
class ProfileAdmin(ModelAdmin):
    model = Army

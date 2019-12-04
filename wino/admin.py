from django.contrib import admin
from .models import *


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country_list']
    ordering = ['id']


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'region']
    ordering = ['id']


@admin.register(Quality)
class QualityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country', 'region', 'area']
    ordering = ['id']


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'quality', 'classification']
    ordering = ['id']

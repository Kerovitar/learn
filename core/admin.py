from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.PoolMaterial)
class PoolMaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PoolType)
class PoolTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Pool)
class PoolAdmin(admin.ModelAdmin):
    pass


@admin.register(models.FountainType)
class FountaintypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.FountainMaterial)
class FountainMaterial(admin.ModelAdmin):
    pass


@admin.register(models.Fountain)
class FountainAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BathMaterial)
class BathMaterial(admin.ModelAdmin):
    pass


@admin.register(models.BathType)
class BathTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Bath)
class BathAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SPAMaterial)
class SPAhMaterial(admin.ModelAdmin):
    pass


@admin.register(models.SPAType)
class SPATypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SPA)
class SPAAdmin(admin.ModelAdmin):
    pass


@admin.register(models.HummumMaterial)
class HummumhMaterial(admin.ModelAdmin):
    pass


@admin.register(models.HummumType)
class HummumTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Hummum)
class HummumAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AutowatMaterial)
class AutowathMaterial(admin.ModelAdmin):
    pass


@admin.register(models.Autowat)
class AutowatAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
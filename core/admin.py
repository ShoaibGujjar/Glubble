from django.contrib import admin

from core.models import GPUSpecs


@admin.register(GPUSpecs)
class GPUSpecsAdmin(admin.ModelAdmin):
    pass

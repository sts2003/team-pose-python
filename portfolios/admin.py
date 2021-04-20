from django.contrib import admin
from . import models


@admin.register(models.PortfoliosModel)
class PortfoliosAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "url",
    )

    filter_horizontal = ("participants",)

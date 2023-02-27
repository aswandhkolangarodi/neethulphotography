from django.contrib import admin

# Register your models here.
from .models import Project,Banner

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "groom_name","bride_name","date")
    list_filter = ("date", )
    search_fields = (
        "name",
        "groom_name",
        "bride_name",
        "date"
    )


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    # list_display = ("name", "groom_name","bride_name","date")
    # list_filter = ("date", )
    search_fields = (
        "name",
        "groom_name",
        "bride_name",
        "date"
    )
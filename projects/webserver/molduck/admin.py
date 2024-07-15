from django.contrib import admin

from molduck.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        # "created_by",
        "success",
    )

    def success(self, obj) -> bool:
        return obj.success

    success.boolean = True

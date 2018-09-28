from django.contrib import admin

from ims.models import CommonCartridge


class CommonCartridgeAdmin(admin.ModelAdmin):
    list_display = ("__str__", "upload_at")


admin.site.register(CommonCartridge, CommonCartridgeAdmin)

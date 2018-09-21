from django.contrib import admin

from ims.models import CommonCartridge


class CommonCartridgeAdmin(admin.ModelAdmin):
    pass


admin.site.register(CommonCartridge, CommonCartridgeAdmin)

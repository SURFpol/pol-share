from django.contrib import admin

from ims.models import CommonCartridge


class CommonCartridgeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'upload_at', 'metadata_tag')


admin.site.register(CommonCartridge, CommonCartridgeAdmin)

from django.contrib import admin

from datagrowth.admin import HttpResourceAdmin
from canvas.models import CanvasIMSCCExport, CanvasIMSCCExportDownload


class CanvasIMSCCExportAdmin(HttpResourceAdmin):
    pass


class CanvasIMSCCExportDownloadAdmin(HttpResourceAdmin):
    pass


admin.site.register(CanvasIMSCCExport, CanvasIMSCCExportAdmin)
admin.site.register(CanvasIMSCCExportDownload, CanvasIMSCCExportDownloadAdmin)

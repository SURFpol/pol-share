from django.contrib import admin

from ims.models import IMSArchive, LTIApp, LTITenant


class IMSArchiveAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at', 'metadata_tag')


class LTIAppAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'description', 'privacy_level', 'created_at', 'modified_at')


class LTITenantAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'organization', 'app', 'client_secret', 'created_at', 'modified_at')


admin.site.register(IMSArchive, IMSArchiveAdmin)
admin.site.register(LTIApp, LTIAppAdmin)
admin.site.register(LTITenant, LTITenantAdmin)

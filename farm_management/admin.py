from django.contrib import admin

from .models.base import AdminMenuMaster


@admin.register(AdminMenuMaster)
class AdminMenuMasterAdmin(admin.ModelAdmin):
    list_display = ('menu_name', 'menu_order', 'menu_icon', 'menu_route', 'menu_access', 'status', 'deleted',
                    'created_at', 'updated_at')

    def has_module_permission(self, request):
        return request.user.is_superuser

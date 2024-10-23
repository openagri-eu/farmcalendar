from django.contrib import admin

from farm_management.models.base import AdminMenuMaster


# class CustomAdminSite(admin.AdminSite):
#     site_header = "Farm Calendar Administration"
#     site_title = "Farm Calendar Admin Portal"
#     index_title = "Welcome to the Farm Calendar Admin"
#
#
# custom_admin_site = CustomAdminSite(name='custom_admin')


@admin.register(AdminMenuMaster)
class AdminMenuMasterAdmin(admin.ModelAdmin):
    list_display = ('menu_name', 'menu_order', 'menu_icon', 'menu_route', 'menu_access', 'status', 'deleted',
                    'created_at', 'updated_at')

    def has_module_permission(self, request):
        return request.user.is_superuser

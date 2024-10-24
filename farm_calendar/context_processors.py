from farm_management.models.base import AdminMenuMaster


def get_admin_menu(request):
    admin_menu = AdminMenuMaster.objects.filter(status=1).order_by('menu_order')

    context_data = {
        'admin_menu': admin_menu
    }

    return context_data

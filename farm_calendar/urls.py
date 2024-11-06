"""
URL configuration for openagri_farm_calendar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include("farm_management.urls")),
    path("", include("farm_activities.urls")),
    path("", include("apis.urls")),
]

# # should be on an apis app
# from harvesthand.views import FarmAreaViewSet, FarmPlantViewSet, FarmAnimalViewSet, FarmEquipmentViewSet
# from farmactivities.views import FarmActivityViewSet, FarmActivityTypeViewSet

# router = routers.DefaultRouter()
# router.register(r'FarmAreas', FarmAreaViewSet)
# router.register(r'FarmPlants', FarmPlantViewSet)
# router.register(r'FarmAnimals', FarmAnimalViewSet)
# router.register(r'FarmEquipments', FarmEquipmentViewSet)
# router.register(r'FarmActivities', FarmActivityViewSet)
# router.register(r'FarmActivityTypes', FarmActivityTypeViewSet)

# urlpatterns += [
#     path('api/', include(router.urls)),
# ]

urlpatterns += staticfiles_urlpatterns()
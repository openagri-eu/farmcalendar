from django.urls import path, include
from rest_framework import routers

from .views import (
    FarmParcelViewSet,
    FarmCropViewSet,
    FarmAnimalViewSet,
    AgriculturalMachineViewSet,
    FarmActivityViewSet,
    FarmActivityTypeViewSet,
)

router = routers.DefaultRouter()
router.register(r'FarmParcels', FarmParcelViewSet)
router.register(r'FarmCrops', FarmCropViewSet)
router.register(r'FarmAnimals', FarmAnimalViewSet)
router.register(r'FarmEquipments', AgriculturalMachineViewSet)
router.register(r'FarmActivities', FarmActivityViewSet)
router.register(r'FarmActivityTypes', FarmActivityTypeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
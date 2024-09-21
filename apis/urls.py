from django.urls import path, include
from rest_framework import routers

from .views import (
    FarmViewSet,
    FarmParcelViewSet,
    FarmCropViewSet,
    FarmAnimalViewSet,
    AgriculturalMachineViewSet,
    FarmOperationViewSet,
    FarmOperationTypeViewSet,
    FertilizationOperationViewSet,
    FertilizerViewSet,
)

router = routers.DefaultRouter()

router.register(r'Farm', FarmViewSet)
router.register(r'FarmParcels', FarmParcelViewSet)
router.register(r'FarmCrops', FarmCropViewSet)
router.register(r'FarmAnimals', FarmAnimalViewSet)
router.register(r'FarmEquipments', AgriculturalMachineViewSet)
router.register(r'FarmOperations', FarmOperationViewSet)
router.register(r'FarmOperationTypes', FarmOperationTypeViewSet)
router.register(r'FertilizationOperation', FertilizationOperationViewSet)
router.register(r'Fertilizer', FertilizerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
from django.urls import path, include
from rest_framework import routers

from .views import (
    FarmParcelViewSet,
    FarmCropViewSet,
    FarmAnimalViewSet,
    AgriculturalMachineViewSet,
    FarmOperationViewSet,
    FarmOperationTypeViewSet,
)

router = routers.DefaultRouter()
router.register(r'FarmParcels', FarmParcelViewSet)
router.register(r'FarmCrops', FarmCropViewSet)
router.register(r'FarmAnimals', FarmAnimalViewSet)
router.register(r'FarmEquipments', AgriculturalMachineViewSet)
router.register(r'FarmOperations', FarmOperationViewSet)
router.register(r'FarmOperationTypes', FarmOperationTypeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
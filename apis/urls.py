from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings

from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


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
    path('api/', lambda request: redirect('api-root', settings.SHORT_API_VERSION)),
    path('api/<str:version>/', include([
        path('', include(router.urls)),  # Register versioned API routes
        path('schema/', SpectacularAPIView.as_view(), name='schema'),  # Schema generation
        path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI
        path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  # ReDoc
    ])),
]
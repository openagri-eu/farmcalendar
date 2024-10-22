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
    FarmCalendarActivityViewSet,
    FarmCalendarActivityTypeViewSet,
    FertilizationOperationViewSet,
    FertilizerViewSet,
    IrrigationOperationViewSet,
    CropProtectionOperationViewSet,
    PesticideViewSet,
    ObservationViewSet,
    CropStressIndicatorObservationViewSet,
    CropGrowthStageObservationViewSet,
)

router = routers.DefaultRouter()

router.register(r'Farm', FarmViewSet)
router.register(r'FarmParcels', FarmParcelViewSet)
router.register(r'FarmCrops', FarmCropViewSet)
router.register(r'FarmAnimals', FarmAnimalViewSet)
router.register(r'AgriculturalMachines', AgriculturalMachineViewSet)
router.register(r'FarmCalendarActivities', FarmCalendarActivityViewSet)
router.register(r'FarmCalendarActivityTypes', FarmCalendarActivityTypeViewSet)
router.register(r'FertilizationOperations', FertilizationOperationViewSet)
router.register(r'Fertilizers', FertilizerViewSet)
router.register(r'IrrigationOperations', IrrigationOperationViewSet)
router.register(r'CropProtectionOperations', CropProtectionOperationViewSet)
router.register(r'Pesticides', PesticideViewSet)
router.register(r'Observations', ObservationViewSet)
router.register(r'CropStressIndicatorObservations', CropStressIndicatorObservationViewSet)
router.register(r'CropGrowthStageObservations', CropGrowthStageObservationViewSet)




urlpatterns = [
    path('api/', lambda request: redirect('api-root', settings.SHORT_API_VERSION)),
    path('api/<str:version>/', include([
        path('', include(router.urls)),  # Register versioned API routes
        path('schema/', SpectacularAPIView.as_view(), name='schema'),  # Schema generation
        path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI
        path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  # ReDoc
    ])),
]
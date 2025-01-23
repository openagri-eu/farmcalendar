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

from django.urls import path
from .views import (
    login_view,
    post_authentication,
    FarmParcelView,
    FarmView,
    AjaxHandlerView,
    FarmCropListView,
    FarmCropUpdateView,
    FarmAnimalListView,
    FarmAnimalUpdateView,
    AgriculturalMachineListView,
    AgriculturalMachineUpdateView,
    FertilizerListView,
    FertilizerUpdateView,
    PesticideListView,
    PesticideUpdateView,
)


urlpatterns = [
    path("login/", login_view, name="login"),
    path("post_auth/", post_authentication, name="post_auth"),
    # Ajax routes for toggling status and deletion
    # this has to be changed to use the actual API, otherwise we are creating two
    # different APIs in the system, and instead we shoud use one if we want to retrieve JSON(or JSON-LD)
    # representation of the models
    path(
        "<str:prefix>/ajax/<str:action>/<uuid:pk>/",
        view=AjaxHandlerView.as_view(),
        name="action",
    ),
    path("farms/", FarmView.as_view(), name="farms"),
    path("farms/<uuid:pk>/", view=FarmView.as_view(), name="farm_edit"),
    path("farm-parcels/", FarmParcelView.as_view(), name="farm_parcels"),
    path("farm-parcels/<uuid:pk>/", view=FarmParcelView.as_view(), name="farm_parcel_edit",),

    path("farm-crops/", FarmCropListView.as_view(), name="farm_crops"),
    path("farm-crops/<uuid:pk>/", FarmCropUpdateView.as_view(), name="farm_crop_edit"),
    path("farm-animals/", FarmAnimalListView.as_view(), name="farm_animals"),
    path("farm-animals/<uuid:pk>/", FarmAnimalUpdateView.as_view(), name="farm_animal_edit"),
    path("agri-machines/", AgriculturalMachineListView.as_view(), name="agri_machines"),
    path("agri-machines/<uuid:pk>/", AgriculturalMachineUpdateView.as_view(), name="agri_machine_edit"),

    path("fertilizers/", FertilizerListView.as_view(), name="fertilizers"),
    path("fertilizers/<uuid:pk>/", FertilizerUpdateView.as_view(), name="fertilizer_edit"),

    path("pesticides/", PesticideListView.as_view(), name="pesticides"),
    path("pesticides/<uuid:pk>/", PesticideUpdateView.as_view(), name="pesticide_edit"),
]
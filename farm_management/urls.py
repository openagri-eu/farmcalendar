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
from . import views
from .views import FarmParcelView, FarmView, AjaxHandlerView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('post_auth/', views.post_authentication, name='post_auth'),

    # Ajax routes for toggling status and deletion
    # this has to be changed to use the actual API, otherwise we are creating two
    # different APIs in the system, and instead we shoud use one if we want to retrieve JSON(or JSON-LD)
    # representation of the models
    path('<str:prefix>/ajax/<str:action>/<int:pk>/', view=AjaxHandlerView.as_view(), name='action'),

    path('farms/', FarmView.as_view(), name='farms'),
    path("farms/edit/<uuid:pk>/", view=FarmView.as_view(), name='farm_edit'),

    path('farm-parcels/', FarmParcelView.as_view(), name='farm_parcels'),
    path('farm-parcels/edit/<uuid:pk>/', view=FarmParcelView.as_view(), name='farm_parcel_edit'),
]

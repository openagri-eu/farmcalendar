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
from .views import FarmParcelView, FarmMasterView, AjaxHandlerView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('post_auth/', views.post_authentication, name='post_auth'),
    path('test_perm/', views.need_permission_view, name='need_permission'),

    # Ajax routes for toggling status and deletion
    path('<str:prefix>/ajax/<str:action>/<int:pk>/', view=AjaxHandlerView.as_view(), name='action'),

    path('farms/', FarmMasterView.as_view(), name="farms"),
    path("farms/edit/<int:pk>/", view=FarmMasterView.as_view(), name="farm_edit"),

    path('farm-parcels/', FarmParcelView.as_view(), name="farm-parcels"),
    path("farm-parcels/edit/<int:pk>/", view=FarmParcelView.as_view(), name="farm-parcel_edit"),
]

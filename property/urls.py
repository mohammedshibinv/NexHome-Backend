from django.urls import path

from .views import PropertiesListView,PropertyDetailsView

urlpatterns = [
    path('', PropertiesListView.as_view(), name='property-list'),
    path('<uuid:pk>/', PropertyDetailsView.as_view(), name='property-details'),
]

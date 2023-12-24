from django.urls import path
from .views import AddToElasticsearch, GetApplicationStatus, GetServiceStatus

urlpatterns = [
    path('add', AddToElasticsearch.as_view(), name='add_to_elasticsearch'),
    path('healthcheck', GetApplicationStatus.as_view(), name='get_application_status'),
    path('healthcheck/<str:service_name>', GetServiceStatus.as_view(), name='get_service_status'),
]

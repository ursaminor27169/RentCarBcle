from django.urls import path
from .views import bicycles, filter_by_stamp, filter_by_type


urlpatterns = [
    path('', bicycles, name='bicycles'),
    path('stamps/<int:stamp_id>/', filter_by_stamp, name='filter_by_stamp'),
    path('type/<int:type_id>/', filter_by_type, name='filter_by_type'),
]
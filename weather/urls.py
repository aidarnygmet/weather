from django.urls import path
from .views import getMeteoData, add_data_to_excel
from . import views
urlpatterns = [
    path('', views.base, name='base'),
    path('getMeteoData/', getMeteoData, name="getMeteoData"),
    path('add_data_to_excel/', add_data_to_excel, name='add_data_to_excel')
    # ... other URL patterns ...
]
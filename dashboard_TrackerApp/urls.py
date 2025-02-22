from django.urls import path
from .views import dashboard_view

app_name = 'dashboard_TrackerApp'

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
]
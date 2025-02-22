# TrackerApp\urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('system/', include('assets_TrackerApp.urls')),
    path('auth/', include('auth_TrackerApp.urls')),
    path('', views.home, name='home'),
    path('profile/', views.user_profile, name='user_profile'),
    path('dashboard/', include('dashboard_TrackerApp.urls', namespace='dashboard_TrackerApp')),
]

handler404 = 'TrackerApp.views.custom_page_not_found'
handler500 = 'TrackerApp.views.custom_error'
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
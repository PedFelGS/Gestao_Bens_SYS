from django.http import request;
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path;
from django.views.generic.base import RedirectView
from . import views

app_name = 'assets_TrackerApp'

urlpatterns = [

    path("", RedirectView.as_view(pattern_name='auth_TrackerApp:login_view'), name='home'),
    
    path('assets/import/', views.asset_import, name='asset_import'),
    path('assets/create/', views.asset_create, name='asset_create'),
    
    path('ativos/', views.asset_list, name='asset_list'),
    path('ativos/<int:id>/', views.asset_detail, name='asset_detail'),
    path('ativos/criar/', views.asset_create, name='asset_create'),
    path('ativos/<int:id>/atualizar/', views.asset_update, name='asset_update'),
    path('ativos/<int:id>/excluir/', views.asset_delete, name='asset_delete'),

    path('categorias/', views.category_list, name='category_list'),
    path('categorias/<int:id>/', views.category_detail, name='category_detail'),
    path('categorias/criar/', views.category_create, name='category_create'),
    path('categorias/<int:id>/atualizar/', views.category_update, name='category_update'),
    path('categorias/<int:id>/excluir/', views.category_delete, name='category_delete'),
    
    path('departamentos/', views.department_list, name='department_list'),
    path('departamentos/<int:id>/', views.department_detail, name='department_detail'),
    path('departamentos/criar/', views.department_create, name='department_create'),
    path('departamentos/<int:id>/atualizar/', views.department_update, name='department_update'),
    path('departamentos/<int:id>/excluir/', views.department_delete, name='department_delete'),
    
    path('fornecedores/', views.supplier_list, name='supplier_list'),
    path('fornecedores/<int:id>/', views.supplier_detail, name='supplier_detail'),
    path('fornecedores/criar/', views.supplier_create, name='supplier_create'),
    path('fornecedores/<int:id>/atualizar/', views.supplier_update, name='supplier_update'),
    path('fornecedores/<int:id>/excluir/', views.supplier_delete, name='supplier_delete'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
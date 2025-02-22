from django.test import TestCase
from django.urls import reverse

class CatalogURLsTest(TestCase):
    def test_asset_list_url_is_correct(self):
      list_url = reverse('assets_TrackerApp:asset_list')
      self.assertEqual(list_url, '/system/ativos/')
    def test_asset_detail_url_is_correct(self):
        asset_id = 3
        detail_url = reverse('assets_TrackerApp:asset_detail', kwargs={'id': asset_id})
        self.assertEqual(detail_url, f'/system/ativos/{asset_id}/')
    def test_asset_create_url_is_correct(self):
        create_url = reverse('assets_TrackerApp:asset_create')
        self.assertEqual(create_url, '/system/ativos/criar/')
    def test_asset_update_url_is_correct(self):
        asset_id = 42
        update_url = reverse('assets_TrackerApp:asset_update', kwargs={'id': asset_id})
        self.assertEqual(update_url, f'/system/ativos/{asset_id}/atualizar/')




    def test_category_list_url_is_correct(self):
        list_url = reverse('assets_TrackerApp:category_list')
        self.assertEqual(list_url, '/system/categorias/')

    def test_category_detail_url_is_correct(self):
         category_id = 12
         detail_url = reverse('assets_TrackerApp:category_detail', kwargs={'id': category_id})
         self.assertEqual(detail_url, f'/system/categorias/{category_id}/')

    def test_category_create_url_is_correct(self):
        create_url = reverse('assets_TrackerApp:category_create')
        self.assertEqual(create_url, '/system/categorias/criar/')

    def test_category_update_url_is_correct(self):
        category_id = 12
        update_url = reverse('assets_TrackerApp:category_update', kwargs={'id': category_id})
        self.assertEqual(update_url, f'/system/categorias/{category_id}/atualizar/')

    def test_category_delete_url_is_correct(self):
        category_id = 12
        delete_url = reverse('assets_TrackerApp:category_delete', kwargs={'id': category_id})
        self.assertEqual(delete_url, f'/system/categorias/{category_id}/excluir/')
    
    def test_home_url_redirects_to_login(self):
        home_url = reverse('home')
        self.assertEqual(home_url, '/')
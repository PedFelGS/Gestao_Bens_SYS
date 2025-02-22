from django.test import TestCase
from django.urls import reverse, resolve
from assets_TrackerApp import views

class CatalogVIEWsTest(TestCase): 
  def test_asset_list_view_is_correct(self):
    view = resolve(reverse('assets_TrackerApp:asset_list'))
    self.assertIs(view.func, views.asset_list)
    
  def test_asset_detail_view_is_correct(self):
      asset_id = 3
      view = resolve(reverse('assets_TrackerApp:asset_detail', kwargs={'id': asset_id}))
      self.assertIs(view.func, views.asset_detail)

  def test_asset_create_view_is_correct(self):
        view = resolve(reverse('assets_TrackerApp:asset_create'))
        self.assertIs(view.func, views.asset_create)

  def test_asset_update_view_is_correct(self):
      asset_id = 42
      view = resolve(reverse('assets_TrackerApp:asset_update', kwargs={'id': asset_id}))
      self.assertIs(view.func, views.asset_update)
  
  def test_asset_delete_view_is_correct(self):
      asset_id = 42
      view = resolve(reverse('assets_TrackerApp:asset_delete', kwargs={'id': asset_id}))
      self.assertIs(view.func, views.asset_delete)
      
      
      
      
  def test_category_list_view_is_correct(self):
        view = resolve(reverse('assets_TrackerApp:category_list'))
        self.assertIs(view.func, views.category_list)

  def test_category_detail_view_is_correct(self):
        category_id = 12
        view = resolve(reverse('assets_TrackerApp:category_detail', kwargs={'id': category_id}))
        self.assertIs(view.func, views.category_detail)

  def test_category_create_view_is_correct(self):
        view = resolve(reverse('assets_TrackerApp:category_create'))
        self.assertIs(view.func, views.category_create)

  def test_category_update_view_is_correct(self):
      category_id = 12
      view = resolve(reverse('assets_TrackerApp:category_update', kwargs={'id': category_id}))
      self.assertIs(view.func, views.category_update)
  
  def test_category_delete_view_is_correct(self):
      category_id = 12
      view = resolve(reverse('assets_TrackerApp:category_delete', kwargs={'id': category_id}))
      self.assertIs(view.func, views.category_delete)
  
  def test_asset_list(self):
    response = self.client.get(reverse('assets_TrackerApp:asset_list'))
    ...
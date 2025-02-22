# assets_TrackerApp\forms.py

from django import forms
from .models import Assets, Categories, Departments, Suppliers

class AssetImportForm(forms.Form):
    csv_file = forms.FileField()

class assetForm(forms.ModelForm):
    availability = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    path = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'}),
        label="URL da Imagem",
        help_text="Insira a URL de uma imagem externa para o ativo",
        assume_scheme='http'
    )
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        label="Imagem do Ativo"
    )

    class Meta:
        model = Assets
        fields = ['rfid_tag','name', 'price', 'category', 'department','supplier', 'image', 'path', 'availability']


class CategoryForm(forms.ModelForm):
    path = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'}),
        label="URL da Categoria",
        help_text="Insira a URL de uma imagem externa para a categoria",
        assume_scheme='http'
    )
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        label="Imagem da Categoria"
    )

    class Meta:
        model = Categories
        fields = ['name', 'image', 'path']
        
class DepartmentForm(forms.ModelForm):
    path = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'}),
        label="URL da Departamento",
        help_text="Insira a URL de uma imagem externa para o departmento",
        assume_scheme='http'
    )
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        label="Imagem do Departamento"
    )

    class Meta:
        model = Departments
        fields = ['name', 'image', 'path']

##

class SupplierForm(forms.ModelForm):
    path = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'}),
        label="URL do Fornecedor",
        help_text="Insira a URL de uma imagem externa para o fornecedor",
        assume_scheme='http'
    )
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        label="Imagem do Fornecedor"
    )

    class Meta:
        model = Suppliers
        fields = ['name', 'image', 'path']

from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from .models import Assets, Categories, Departments, Suppliers

class AssetResource(resources.ModelResource):
    category = Field(
        column_name='categoria',
        attribute='category',
        widget=ForeignKeyWidget(Categories, 'name')
    )
    department = Field(
        column_name='departamento',
        attribute='department',
        widget=ForeignKeyWidget(Departments, 'name')
    )
    supplier = Field(
        column_name='fornecedor',
        attribute='supplier',
        widget=ForeignKeyWidget(Suppliers, 'name')
    )

    class Meta:
        model = Assets
        fields = (
            'id',
            'rfid_tag',
            'name',
            'price',
            'category',
            'department',
            'supplier',
            'availability'
        )
        import_id_fields = ('rfid_tag',)
        export_order = fields
        skip_unchanged = True
        report_skipped = False
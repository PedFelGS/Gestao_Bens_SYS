from django.db import models
from django.db.models import CharField, DateTimeField, AutoField, ForeignKey, DecimalField, PositiveIntegerField, BooleanField, URLField, ImageField;
from auth_TrackerApp.models import User
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

class Categories(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255, unique=True, verbose_name='Nome da Categoria')
    image = ImageField(upload_to='post_img/categories', blank=True, null=True)
    path =  URLField(max_length=2000, verbose_name='Caminho da Imagem', blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    
    @mark_safe
    def figure(self):
        return f'<img width="30px" src="/media/{self.image}">'

    def __str__(self):
        return self.name

class Departments(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255, unique=True, verbose_name='Nome do departamento')
    image = ImageField(upload_to='post_img/departments', blank=True, null=True)
    path =  URLField(max_length=2000, verbose_name='Caminho da Imagem', blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    
    @mark_safe
    def figure(self):
        return f'<img width="30px" src="/media/{self.image}">'

    def __str__(self):
        return self.name

class Suppliers(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255, unique=True, verbose_name='Nome do fornecedor')
    image = ImageField(upload_to='post_img/suppliers', blank=True, null=True)
    path =  URLField(max_length=2000, verbose_name='Caminho da Imagem', blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    
    @mark_safe
    def figure(self):
        return f'<img width="30px" src="/media/{self.image}">'

    def __str__(self):
        return self.name

class Assets(models.Model):
    id = AutoField(primary_key=True)
    rfid_tag = models.CharField(
        max_length=50, 
        unique=True, 
        verbose_name='Tag RFID'
    )
    name = CharField(max_length=255, verbose_name='Nome do Ativo')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor do Ativo')
    category = ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        verbose_name='Categoria',
        null=True,
        related_name="assets"
        )
    department = models.ForeignKey(
        Departments,
        on_delete=models.SET_NULL,
        verbose_name='Departamento',
        null=True,
        related_name="assets"
    )
    supplier = models.ForeignKey(
        Suppliers,
        on_delete=models.SET_NULL,
        verbose_name='Fornecedor',
        null=True,
        related_name="assets"
    )
    image = ImageField(upload_to='post_img/assets', blank=True, null=True)
    path = URLField(max_length=2000, verbose_name='Caminho da Imagem', blank=True, null=True)
    availability = BooleanField(default=False, verbose_name='Disponibilidade')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    
    @mark_safe
    def figure(self):
        return f'<img width="30px" src="/media/{self.image}">'

    def __str__(self):
        return self.name
    
    def clean(self):
        if self.price <= 0:
            raise ValidationError("O valor deve ser um numero positivo")
    
from django.utils import timezone

class Movements(models.Model):
    id = models.AutoField(primary_key=True)
    asset = models.ForeignKey(
        Assets,
        on_delete=models.CASCADE,
        verbose_name='Ativo',
        related_name='movements'
    )
    origin_dept = models.ForeignKey(
        Departments,
        on_delete=models.PROTECT,
        verbose_name='Departamento de Origem',
        related_name='movements_origin'
    )
    destination_dept = models.ForeignKey(
        Departments,
        on_delete=models.PROTECT,
        verbose_name='Departamento de Destino',
        related_name='movements_destination'
    )
    responsible = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='Responsável',
        null=True,
        blank=True
    )
    movement_date = models.DateTimeField(
        verbose_name='Data da Movimentação',
        default=timezone.now
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.asset.name} movido de {self.origin_dept.name} para {self.destination_dept.name}"

    class Meta:
        verbose_name = 'Movimentação'
        verbose_name_plural = 'Movimentações'
        ordering = ['-movement_date']

    def clean(self):
        if self.origin_dept == self.destination_dept:
            raise ValidationError("Departamento de origem e destino devem ser diferentes")
        
        if self.movement_date > timezone.now():
            raise ValidationError("Data da movimentação não pode ser futura")
            
        if self.asset.department != self.origin_dept:
            raise ValidationError("O ativo não pertence ao departamento de origem informado")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

        self.asset.department = self.destination_dept
        self.asset.save()
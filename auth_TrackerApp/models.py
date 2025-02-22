import uuid
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.db.models.fields import CharField, EmailField, BooleanField, DateTimeField, UUIDField;

class User(models.Model):
    ROLE_CHOICES = [
        ('cliente', 'Cliente'),
        ('gerenciador', 'Gerenciador'),
    ]
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = CharField(max_length=255)
    email = EmailField(unique=True)
    password_hash = CharField(max_length=255)
    admin = BooleanField(default=False)
    role = CharField(max_length=20, choices=ROLE_CHOICES, default='cliente')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def set_password(self, raw_password):
        self.password_hash = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password_hash)

    def __str__(self):
        return self.name
    

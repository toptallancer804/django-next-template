from django.db import models
from controllers.jwt_auth.models import *

# Create your models here.

class Owner(models.Model):
    name = models.TextField(max_length=255)
    name_furi = models.TextField(max_length=255)
    address = models.TextField(max_length=255)
    phone = models.TextField(max_length=255)
    fax = models.TextField(max_length=255)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
class OwnerMember(models.Model):
    ROLE_CHOICES = (
        ("owner", 'Owner'),
        ("admin", 'Admin'),
        ("member", 'Member')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    first_name_furi = models.TextField(max_length=255)
    last_name_furi = models.TextField(max_length=255)
    department = models.TextField(max_length=255)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="member")

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
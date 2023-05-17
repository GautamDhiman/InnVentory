from django.db import models

class BaseModel(models.Model):
    """"""
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)

    class Meta:
        abstract = True
        default_permissions = ('add', 'change', 'delete', 'view')
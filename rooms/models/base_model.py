from django.db import models

class BaseModel(models.Model):
    """"""
    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    updated_by = models.CharField(max_length=100)

    class Meta:
        abstract = True
        default_permissions = ('add', 'change', 'delete', 'view')
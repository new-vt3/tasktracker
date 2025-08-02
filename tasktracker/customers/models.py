from django_tenants.models import TenantMixin, DomainMixin
from django.db import models

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField(null=True, blank=True)         # Make sure this exists
    on_trial = models.BooleanField(default=True)                 # Optional but recommended
    created_on = models.DateField(auto_now_add=True)             # Optional but recommended
    auto_create_schema = True

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    pass

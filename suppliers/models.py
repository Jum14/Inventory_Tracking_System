from django.db import models

class Supplier(models.Model):
    # Django automatically creates an 'id' field for us
    company_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    is_active = models.BooleanField(default=True) # Fulfills the 5+ fields rule

    def __str__(self):
        # This makes the object show up as the company name in the admin panel
        return self.company_name
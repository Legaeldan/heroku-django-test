from django.db import models

# Create your models here.
# Model for new table in db
class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)

    # Adds a readable item name in admin panel in new table.
    def __str__(self):
        return self.name

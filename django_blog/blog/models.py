from django.db import models
from datetime import datetime

class Record (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    create_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
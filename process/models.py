from django.db import models


class BTCAddress(models.Model):
    
    Address = models.CharField(max_length=200) 

    def __str__(self):
        return self.Address

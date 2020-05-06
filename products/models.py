from django.db import models

# Create your models here.
class product(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=20)
    description=models.TextField(max_length=30,blank=True, null=True)
    price=models.DecimalField(max_digits=20000,decimal_places=2)


    def __str__(self):
        return self.name
from django.db import models

class contact(models.Model):
     name = models.CharField(max_length=100)
     title = models.CharField(max_length=100)
     email = models.EmailField(max_length=30)
     
     def _str_(self):
         return self.name
         


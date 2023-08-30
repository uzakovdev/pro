from django.db import models

# Create your models here.


class Mypro(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

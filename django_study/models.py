from django.db import models

# Create your models here.
class Kimetsu(models.Model):
    name = models.CharField(max_length=100, verbose_name="名前")
    sex = models.CharField(max_length=2, verbose_name="性別")
    feature = models.CharField(max_length=100, verbose_name="特徴")

    def __str__(self):
        return self.name
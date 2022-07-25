from django.db import models

# Create your models here.


class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state =  models.CharField(max_length=2,default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)

    object = models.Manager()

    class Meta:
        verbose_name_plural = "UniversityCampus"



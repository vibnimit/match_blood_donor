from django.db import models


class BloodDonatingUsers(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    phone = models.CharField(max_length=20)
    label = models.IntegerField()
    blood_group = models.CharField(max_length=5)

    def __unicode__(self):
        return "%s :: %s" %(self.name, self.blood_group)
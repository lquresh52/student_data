from django.db import models

# Create your models here.
class StudetData(models.Model):
    name = models.CharField(max_length=300)
    standard = models.IntegerField()
    roll_no = models.IntegerField()
    age = models.IntegerField()
    mobile_no_p1 = models.BigIntegerField()
    mobile_no_p2 = models.BigIntegerField(blank=True,null=True)

    def __str__(self):
        return self.name
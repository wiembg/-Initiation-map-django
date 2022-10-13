from django.db import models

# Create your models here.




# Create your models here.
class AllData(models.Model):
    id = models.AutoField(primary_key=True)
    Indicator = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    ADM1_CODE = models.FloatField(default=0)
    Province = models.CharField(max_length=100)
    Land_Type = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    Data = models.FloatField(default=0)
    Data_long_term_Average = models.FloatField(default=0)
    Year = models.FloatField(default=0)
    Month = models.FloatField(default=0)
    Dekad = models.FloatField(default=0)
    Unit = models.FloatField(default=0)
    Source = models.CharField(max_length=100)

    def __str__(self):
        return self.Country



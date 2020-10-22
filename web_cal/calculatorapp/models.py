from django.db import models

# Create your models here.


# Create your models here.
class Calculations(models.Model):
    operand1 = models.CharField(max_length=15)
    operator = models.CharField(max_length=1)
    operand2 = models.CharField(max_length=15)
    results = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.operand1 + self.operator + self.operand2 + self.results

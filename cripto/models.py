from django.db import models


class CandleStick(models.Model):
    euro = models.CharField(max_length=20)
    dolar = models.CharField(max_length=20)
    jpy = models.CharField(max_length=20)
    real = models.CharField(max_length=20)
    period = models.DateTimeField()

    class Meta:
        managed = True
        verbose_name = 'CandleStick'
        unique_together = ('dolar', 'period')

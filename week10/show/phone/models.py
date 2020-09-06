from django.db import models


class SmzdmPhone(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.CharField(max_length=255)
    dt = models.CharField(max_length=25)
    content = models.TextField()
    # sentiments = models.CharField(max_length=25)
    sentiments = models.FloatField(max_length=25)
    updatedt = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'smzdm_phone'

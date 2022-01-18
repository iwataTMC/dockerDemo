from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class GPS(models.Model):
    # 緯度
    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
    )
    # 経度
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(-180)],
    )

    def save(self, *args, **kwargs):
        latitude = kwargs.pop('latitude', None)
        longitude = kwargs.pop('longitude', None)

        # 有効値のみ保存
        if latitude is not None and longitude is not None:
            self.latitude = float(latitude)
            self.longitude = float(longitude)
            super().save(*args, **kwargs)

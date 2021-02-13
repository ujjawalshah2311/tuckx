from django.db import models

# Create your models here.
class dashcam(models.Model):
    imei=models.CharField(max_length=10)
    location_time = models.CharField(max_length=10,null=True)
    latitude = models.CharField(max_length=10,null=True)
    longitude = models.CharField(max_length=10,null=True)

    def _str_(self):
        return self.imei

class dashcamvideo(models.Model):
    imei=models.CharField(max_length=10)
    filename=models.CharField(max_length=10)
    video = models.FileField(upload_to="myapi/video")

    def _str_(self):
        return self.imei

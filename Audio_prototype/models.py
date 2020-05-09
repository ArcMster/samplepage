from django.db import models

# Create your models here.
class Audios(models.Model):
    audio_id = models.CharField(max_length=20)
    audio_file = models.FileField(upload_to='media')
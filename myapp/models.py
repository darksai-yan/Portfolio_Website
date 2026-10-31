from django.db import models

# Create your models here.
class ArtWork(models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateField()
    description = models.TextField()
    photos = models.ImageField(upload_to='artworks_photos/%Y/%m/', blank=True, null=True)


    def __str__(self):
        return self.title
    
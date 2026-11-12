from django.db import models

# Create your models here.

from django.db import models
from urllib.parse import urlparse, parse_qs

class ArtWork(models.Model):

    ARTWORK_TYPES = [
        ('2d', '2D'),
        ('3d', '3D'),
    ]

    MEDIA_TYPES = [
        ('photo', 'Photo'),
        ('video', 'Video'),
        ('gif', 'GIF'),
    ]

    title = models.CharField(max_length=200)
    date_created = models.DateField()
    description = models.TextField()

    photos = models.ImageField(
        upload_to='artworks_photos/%Y/%m/',
        blank=True,
        null=True
    )

    video_url = models.URLField(
        blank=True,
        verbose_name='YouTube Video URL'
    )

    media_type = models.CharField(
        max_length=5,
        choices=MEDIA_TYPES,
        default='photo',
        verbose_name='Media Type'
    )

    is_best = models.BooleanField(
        default=False,
        verbose_name='Best Artwork'
    )

    artwork_type = models.CharField(
        max_length=2,
        choices=ARTWORK_TYPES,
        default='2d',
        verbose_name='Artwork Type'
    )

    @property
    def youtube_embed_url(self):
        url = self.video_url.strip()

        parsed = urlparse(url)
        video_id = ''

        if parsed.hostname in ('youtube.com', 'www.youtube.com', 'm.youtube.com'):
            if parsed.path == '/watch':
                video_id = parse_qs(parsed.query).get('v', [''])[0]

            elif parsed.path.startswith(('/embed/', '/shorts/')):
                video_id = parsed.path.split('/')[-1]

        elif parsed.hostname in ('youtu.be', 'www.youtu.be'):
            video_id = parsed.path.strip('/').split('/')[0]

        if video_id:
            return f'https://www.youtube-nocookie.com/embed/{video_id}'

        return ''
    def __str__(self):
        return self.title
    
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # Post é um modelo de django e poderá ser salvo no BD.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    # TextField nao tem limite de chars.
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        #metodo publicar.
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

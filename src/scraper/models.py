from django.db import models

from django.conf import settings
# Create your models here.



class Article(models.Model):
    source = models.CharField(max_length=30)
    title = models.CharField(max_length=150)
    url = models.TextField()
    detail = models.TextField()
    added_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    last_scrape = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{}-{}".format(self.user, self.last_scrape)





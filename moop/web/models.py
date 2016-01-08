from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Image(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


class Collection(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.name

    
class Tag(models.Model):
    name = models.CharField(max_length=30)
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.name


# Signals

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

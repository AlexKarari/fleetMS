from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from sacco.models import Sacco

# Create your models here.


class Owner(models.Model):

    nat_id = models.IntegerField(unique=True, default=00000000)
    email = models.EmailField()
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    telephone = models.IntegerField(unique=True, blank=True)
    profile_pic = models.ImageField(upload_to='ownerProfile/', blank=True)
    sacco = models.ForeignKey(Sacco)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def update_owner(sender, instance, created, **kwargs):
        if created:
            Owner.objects.create(user=instance)
        instance.owner.save()


class Vehicle(models.Model):
    number_plate = models.CharField(max_length=200)
    capacity = models.IntegerField()

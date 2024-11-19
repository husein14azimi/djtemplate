# account.signals

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Person
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_person(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_person(sender, instance, **kwargs):
    instance.person.save()
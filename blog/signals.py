from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Blog, Notification
import logging


@receiver(post_save, sender=Blog)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(message=f"New Blog Post: {instance.title}")


@receiver(post_save, sender=Blog)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(message=f"New Blog Post: {instance.title}")
        logger = logging.getLogger('blog.signals')
        logger.info(f"New Blog Post: {instance.title}")
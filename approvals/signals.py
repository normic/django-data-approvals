from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.conf import settings

from .models import Approval


@receiver(pre_save)
def model_pre_save(sender, **kwargs):
    print('Should be saved: {}'.format(kwargs['instance'].__dict__))

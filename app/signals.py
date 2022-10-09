from django.db.models.signals import post_save,pre_delete
from accounts.models import User
from django.dispatch import receiver
from .models import Complain,Status


@receiver(post_save,sender =Complain)
def post_save_create_profile(sender,instance,created,**kwargs):
    if created:
        Status.objects.create(post = instance)

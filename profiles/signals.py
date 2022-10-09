from django.db.models.signals import post_save,pre_delete
from accounts.models import User
from django.dispatch import receiver
from .models import Student,Teacher


@receiver(post_save,sender =User)
def post_save_create_profile(sender,instance,created,**kwargs):

    if instance.code == 'ruetteachers1234':
        if created:
            Teacher.objects.create(user = instance)
    else:
        if created:
            Student.objects.create(user = instance)
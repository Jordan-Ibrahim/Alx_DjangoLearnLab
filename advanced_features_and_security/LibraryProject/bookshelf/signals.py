from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver 

@receiver(post_migrate)


def create_group(sender,**kwargs):
 if sender.name == "bookshelf":
   app_label = "bookshelf"
   can_view = Permission.objects.get(codename="can_view", content_type__app_label=app_label)
   can_create = Permission.objects.get(codename="can_create", content_type__app_label=app_label)
   can_edit = Permission.objects.get(codename="can_edit", content_type__app_label=app_label)
   can_delete = Permission.objects.get(codename="can_delete", content_type__app_label=app_label)
   viewers, _ = Group.objects.get_or_create(name="Viewers")
   editors, _ = Group.objects.get_or_create(name="Editors")
   admins, _ = Group.objects.get_or_create(name="Admins")
   viewers.permissions.set([can_view])
   editors.permissions.set([can_view, can_create, can_edit])
   admins.permissions.set([can_view, can_create, can_edit, can_delete])
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Group

@receiver(post_save, sender=CustomUser)
def add_user_to_group(sender, instance, created, **kwargs):
    if instance.group_id:
        group = instance.group_id
        group.users.add(instance)
        group.save()
        users_in_group = group.users.all()
        if users_in_group.exists():
            total_ranking = sum(user.reyting for user in users_in_group if user.ranking is not None)
            user_count = users_in_group.count()
            average_ranking = total_ranking / user_count if user_count > 0 else 0
            group.rate = average_ranking
            group.save()
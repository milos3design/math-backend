from django.dispatch import receiver
from djoser.signals import user_activated
from .models import Consent

@receiver(user_activated)
def create_consent_entry(sender, user, request, **kwargs):
    Consent.objects.create(user=user)
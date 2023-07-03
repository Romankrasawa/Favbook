from .models import *
import re
from django.core.exceptions import ValidationError
from django.conf import settings as conf_settings
import logging

logger = logging.getLogger(__name__)


def validate_user_username(instance):
    username = instance.cleaned_data["username"]
    if (
        username != instance.request.user.username
        and User.objects.filter(username__iexact=username).exists()
    ):
        raise ValidationError("Назва не повинна починатись з цифри")
    if re.match("@", username):
        raise ValidationError("Назва не повинна починатись з цифри")
    return username

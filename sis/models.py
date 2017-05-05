from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Sum
from django.db import connection
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from django.conf import settings
from constance import config

import logging
from django_thumbs.db.models import ImageWithThumbsField
from datetime import date
from custom_field.custom_field import CustomFieldModel
import sys
from ckeditor.fields import RichTextField
from django_cached_field import CachedDecimalField
from decimal import Decimal

from sis.helper_functions import round_as_decimal

logger = logging.getLogger(__name__)

def create_faculty(instance, make_user_group=True):
    """ Create a sis.Faculty object that is linked to the given
    auth_user instance. Important as there is no way to do this
    from Django admin. See
    http://stackoverflow.com/questions/4064808/django-model-inheritance-create-sub-instance-of-existing-instance-downcast
    """
    if not hasattr(instance, "student") and not hasattr(instance, "faculty"):
        faculty = Faculty(user_ptr_id=instance.id)
        faculty.__dict__.update(instance.__dict__)
        faculty.save(make_user_group=make_user_group)

def create_student(instance):
    """ Create a sis.Student object that is linked to the given auth_user
    instance. See create_faculty for more details.
    """
    if not hasattr(instance, "student") and not hasattr(instance, 'faculty'):
        student = Student(user_ptr_id=instance.id)
        student.__dict__.update(instance.__dict__)
        student.save()

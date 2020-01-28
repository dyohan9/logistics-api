from django.utils.translation import gettext as _
from rest_framework.exceptions import ValidationError

from core.common.models import Map


class MapNameNotExistValidator(object):
    def __call__(self, attrs):
        print(attrs)
        map_name = attrs.get("map_name")

        if Map.objects.filter(map_name=map_name).count():
            raise ValidationError(_("Map Name already exists"))


class LogisticTextValidator(object):
    def __call__(self, attrs):
        logistic_text = attrs.get("logistic_text")

        if len(logistic_text) < 0:
            raise ValidationError(_("logistic_text cannot be empty"))

        logistic_text = logistic_text.split(sep="\n", maxsplit=1)
        if len(logistic_text) > 0:
            if len(logistic_text[0].split()) != 3:
                raise ValidationError(_("logistic_text with format invalid2"))
            if not logistic_text[0].split()[-1].isdigit():
                raise ValidationError(_("logistic_text with format invalid3"))

from django.db import models
from django.utils.translation import gettext as _

from core.authentication.models import User


class Map(models.Model):
    class Meta:
        verbose_name = _("Map")

    map_name = models.CharField(_("map name"), max_length=64, help_text=_("Map Name"))
    user = models.ForeignKey(User, models.CASCADE)


class Router(models.Model):
    class Meta:
        verbose_name = _("Router")

    source = models.TextField(_("source"), help_text=_("Point of Origin"))
    destiny = models.TextField(_("destiny"), help_text=_("Point of Destiny"))
    distance = models.IntegerField(_("Distance"), help_text=_("Distance in Kilometers"))
    map = models.ForeignKey(Map, models.CASCADE)

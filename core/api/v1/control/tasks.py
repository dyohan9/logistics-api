import re

from core.celery import app
from core.common.models import Router, Map


@app.task(name="map_create")
def map_create(instance, logistic):
    instance = Map.objects.get(pk=instance)

    for router in logistic:
        regex = [x.group() for x in re.finditer(r"\S+", router)]
        Router.objects.create(
            source=regex[0], destiny=regex[1], distance=regex[2], map=instance
        )
    return True

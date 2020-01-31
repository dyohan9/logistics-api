from rest_framework import serializers

from core.api.v1.control.tasks import map_create
from core.api.v1.control.validators import (
    MapNameNotExistValidator,
    LogisticTextValidator,
)
from core.common.models import Router, Map


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ["id", "map_name", "logistic_text"]
        ref_name = None

    logistic_text = serializers.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(MapNameNotExistValidator())
        self.validators.append(LogisticTextValidator())

    def create(self, validated_data):
        logistic = validated_data.pop("logistic_text").splitlines()
        instance = self.Meta.model(
            map_name=validated_data.get("map_name"), user=self.context["request"].user
        )
        instance.save()

        map_create.delay(instance.pk, logistic)

        return instance


class RouterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Router
        fields = ["source", "destiny", "distance", "map"]
        ref_name = None

    map = MapSerializer(read_only=True)
    distance = serializers.IntegerField(read_only=True)


class SearchSerializer(serializers.Serializer):
    source = serializers.CharField(required=True)
    destiny = serializers.CharField(required=True)
    map_name = serializers.CharField(required=True, max_length=64)
    autonomy = serializers.IntegerField(required=True)
    liter_value = serializers.FloatField(required=True)

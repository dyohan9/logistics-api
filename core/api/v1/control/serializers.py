import re

from rest_framework import serializers

from core.common.models import Router, Map


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ["id", "map_name", "logistic_text"]
        ref_name = None

    logistic_text = serializers.CharField(required=False)

    def create(self, validated_data):
        logistic = validated_data.pop("logistic_text").split("\n")
        instance = self.Meta.model(
            map_name=validated_data.get("map_name"), user=self.context["request"].user
        )
        instance.save()

        for router in logistic:
            regex = [x.group() for x in re.finditer(r"\S+", router)]
            Router.objects.create(
                source=regex[0], destiny=regex[1], distance=regex[2], map=instance
            )

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

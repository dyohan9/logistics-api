from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from core.api.v1.control.serializers import (
    RouterSerializer,
    MapSerializer,
    SearchSerializer,
)
from core.common.models import Router, Map
from core.dijkstra import Graph
from ..metadata import Metadata


class MapViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Map.objects
    serializer_class = MapSerializer
    permission_classes = [IsAuthenticated]
    metadata_class = Metadata


class RouterViewSet(GenericViewSet):
    """
    Search the shortest route according to the fuel price.
    """

    queryset = Router.objects
    serializer_class = RouterSerializer
    permission_classes = [IsAuthenticated]
    metadata_class = Metadata

    @action(
        detail=True,
        methods=["POST"],
        url_name="router-search",
        serializer_class=SearchSerializer,
        permission_classes=[],
    )
    def search(self, request, **kwargs):
        serializer = RouterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        map_name = request.data.get("map_name")
        source = request.data.get("source")
        destiny = request.data.get("destiny")
        autonomy = request.data.get("autonomy")
        liter_value = request.data.get("liter_value")

        routers = Router.objects.filter(map__map_name=map_name)

        result = {}

        if routers:
            grafo = Graph()
            nodes = []
            for r in routers:
                if r.source not in nodes:
                    nodes.append(r.source)
                if r.destiny not in nodes:
                    nodes.append(r.destiny)

                grafo.add_edge(r.source, r.destiny, r.distance)

            grafo.add_node(nodes)

            km, path = grafo.caminho(source, destiny)

            result = {"path": path, "cost": ((liter_value / autonomy) * km)}

        return Response(result)

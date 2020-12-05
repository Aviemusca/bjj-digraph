from rest_framework import generics
from django.shortcuts import get_object_or_404
from drf_multiple_model.views import FlatMultipleModelAPIView

from graphs.models import Graph
from .models import Node, GameNode, MetaNode
from .serializers import NodeSerializer, GameNodeSerializer, MetaNodeSerializer
from utils.views.permissions import IsGraphOwnerOrReadOnly


formatters = {
    "baseNode": {"model": Node, "serializer_class": NodeSerializer, "list": False},
    "gameNode": {
        "model": GameNode,
        "serializer_class": GameNodeSerializer,
        "list": True,
    },
    "metaNode": {
        "model": MetaNode,
        "serializer_class": MetaNodeSerializer,
        "list": True,
    },
}


class NodeAPIViewMixin:
    """A mixin for node api views with helper and selector methods for getting
    the node queryset and model for an incoming request
    """

    def get_graph_id(self):
        """ Returns the graph id from the url """
        graph_id = self.request.resolver_match.kwargs["graph_id"]
        return graph_id

    def get_queryset_(self):
        """ Returns the correct queryset for the node type """
        node_type = self.request.data["type"]
        return formatters[node_type]["model"].objects.all()

    def get_serializer_class_(self):
        """ Returns the correct serializer class for the node type """
        node_type = self.request.data["type"]
        return formatters[node_type]["serializer_class"]


class NodeCreate(NodeAPIViewMixin, generics.CreateAPIView):
    """An API view for creating nodes of different types.
    The node type is required in the body of the request.
    """

    permission_classes = [IsGraphOwnerOrReadOnly]

    def get_serializer_class(self):
        return self.get_serializer_class_()

    def perform_create(self, serializer):
        graph_id = self.get_graph_id()
        graph = get_object_or_404(Graph, id=graph_id)
        serializer.save(graph=graph)


class NodeDetail(NodeAPIViewMixin, generics.RetrieveUpdateDestroyAPIView):
    """A detail API view for RUD operations on nodes of different types.
    The node type is required in the body of the request.
    """

    permission_classes = [IsGraphOwnerOrReadOnly]
    lookup_field = "id"
    lookup_url_kwarg = "node_id"

    def get_queryset(self):
        return self.get_queryset_()

    def get_serializer_class(self):
        return self.get_serializer_class_()


class NodeList(NodeAPIViewMixin, FlatMultipleModelAPIView):
    """A List API view for retrieving all nodes of a graph (multiple types)."""

    def get_querylist(self):
        querylist = [
            {
                "queryset": formatter["model"].objects.of_graph(self.get_graph_id()),
                "serializer_class": formatter["serializer_class"],
            }
            for _, formatter in formatters.items()
            if formatter["list"]
        ]
        return querylist

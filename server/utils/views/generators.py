from rest_framework import generics

from .permissions import IsGraphOwnerOrReadOnly
from .mixins import GraphChildViewMixin, GraphChildListCreateViewMixin


def detail_view_generator(model, serializer, url_kwarg):
    """An API detail view generator for RUD operations on individual
    bjj digraph children, e.g. nodes and edges"""

    class DetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = model.objects.all()
        serializer_class = serializer
        permission_classes = [IsGraphOwnerOrReadOnly]

        lookup_field = "id"
        lookup_url_kwarg = url_kwarg

    return DetailView


def list_view_generator(model, serializer):
    """ An API view generator for listing and creating bjj digraph children """

    class ListView(
        GraphChildViewMixin, GraphChildListCreateViewMixin, generics.ListCreateAPIView
    ):
        queryset = model.objects.all()
        serializer_class = serializer

        def __init__(self, *args, **kwargs):
            """Overwrite init to associate the model with the view
            Doing this so that can call self.model in Mixin instead of passing
            the class directly throughout methods"""
            super().__init__(*args, **kwargs)
            self.model = model

        def perform_create(self, serializer):
            """ Add the graph to the node object. """
            self.perform_create_(serializer)

        def list(self, request, graph_id):
            """ Return all the nodes of a given graph """
            return self.list_(request, graph_id)

    return ListView

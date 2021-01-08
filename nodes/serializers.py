from rest_framework import serializers
from .models import Node, ScoreNode, MetaNode


class NodeSerializer(serializers.ModelSerializer):
    """ A class to serialize bjj digraph base-nodes """

    id = serializers.UUIDField(required=False)
    nodeType = serializers.CharField(source="node_type")
    graph = serializers.ReadOnlyField(source="graph.id")
    createdAt = serializers.DateTimeField(source="created_at", required=False)
    x = serializers.FloatField(source="position_x", required=False)
    y = serializers.FloatField(source="position_y", required=False)

    class Meta:
        model = Node
        fields = (
            "id",
            "nodeType",
            "graph",
            "title",
            "createdAt",
            "x",
            "y",
        )


class ScoreNodeSerializer(NodeSerializer):
    """ A class to serialize bjj digraph score-nodes """

    description = serializers.CharField(required=False, allow_blank=True)
    comment = serializers.CharField(required=False, allow_blank=True)
    effectiveness = serializers.IntegerField(required=False)
    priority = serializers.IntegerField(required=False)
    proficiency = serializers.IntegerField(required=False)

    class Meta:
        model = ScoreNode
        fields = NodeSerializer.Meta.fields + (
            "description",
            "comment",
            "effectiveness",
            "priority",
            "proficiency",
        )


class MetaNodeSerializer(NodeSerializer):
    """ A class to serialize bjj digraph meta-nodes """

    description = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = MetaNode
        fields = NodeSerializer.Meta.fields + ("description",)
        
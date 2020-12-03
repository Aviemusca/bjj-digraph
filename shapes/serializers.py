from rest_framework import serializers
from .models import NodeShape, GameNodeShape, MetaNodeShape


class NodeShapeSerializer(serializers.ModelSerializer):
    """ A class to serialize node shapes """

    id = serializers.UUIDField(required=False)
    owner = serializers.ReadOnlyField(source="owner.id")
    shapeId = serializers.CharField(source="shape_id")
    fill = serializers.CharField(source="fill")
    stroke = serializers.CharField(source="stroke")
    strokeWidth = serializers.CharField(source="stroke_width")

    class Meta:
        model = NodeShape
        fields = (
            "id",
            "owner",
            "shapeId",
            "fill",
            "stroke",
            "strokeWidth",
        )


class GameNodeShapeSerializer(NodeShapeSerializer):
    """ A class to serialize game-node shapes """

    type = serializers.CharField(source="game_type")
    subtype = serializers.CharField(source="game_subtype")

    class Meta:
        model = GameNode
        fields = (
            "id",
            "owner",
            "type",
            "subtype",
            "shapeId",
            "fill",
            "stroke",
            "strokeWidth",
        )


class MetaNodeShapeSerializer(NodeShapeSerializer):
    """ A class to serialize meta-node shapes """

    type = serializers.CharField(source="meta_type")

    class Meta:
        model = MetaNode
        fields = (
            "id",
            "owner",
            "type",
            "shapeId",
            "fill",
            "stroke",
            "strokeWidth",

        )

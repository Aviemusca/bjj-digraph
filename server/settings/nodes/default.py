COMMON_NODE_PROPS = {
    "stroke": "#333333",
    "stroke_width": 2,
    "user_opacity": 0.8,
    "opponent_opacity": 0.5,
}

POSITION = {
    "shape_id": "square",
    "type_text": "New Position",
    "fill": "#ad560e",
    "stroke": COMMON_NODE_PROPS["stroke"],
    "stroke_width": COMMON_NODE_PROPS["stroke_width"],
}

SUBMISSION = {
    "shape_id": "complex-circle",
    "type_text": "New Submission",
    "fill": "#C62525",
    "stroke": COMMON_NODE_PROPS["stroke"],
    "stroke_width": COMMON_NODE_PROPS["stroke_width"],
}

TRANSITION = {
    "shape_id": "skinny-rectangle",
    "type_text": "New Transition",
    "fill": "#9f4ae0",
    "stroke": COMMON_NODE_PROPS["stroke"],
    "stroke_width": COMMON_NODE_PROPS["stroke_width"],
}

ENTRY = {
    "shape_id": "hexagon-pointed",
    "type_text": "New Entry",
    "fill": "#86fa5c",
    "stroke": COMMON_NODE_PROPS["stroke"],
    "stroke_width": COMMON_NODE_PROPS["stroke_width"],
}

ACTION = {
    "shape_id": "lozenge",
    "type_text": "New Action",
    "fill": "#86fade",
    "stroke": COMMON_NODE_PROPS["stroke"],
    "stroke_width": COMMON_NODE_PROPS["stroke_width"],
}

TEXT = {
    "shape_id": "square",
    "type_text": "New Text",
    "fill": "transparent",
    "fill_opacity": "0",
    "stroke": "transparent",
    "stroke_width": "0",
}

COMMENT = {
    "shape_id": "square",
    "type_text": "New Comment",
    "fill": "#bbbbbb",
    "fill_opacity": COMMON_NODE_PROPS["user_opacity"],
    "stroke": COMMON_NODE_PROPS["stroke"],
    "stroke_width": COMMON_NODE_PROPS["stroke_width"],
}

BASE_SCORE_NODE_SETTINGS = {
    "position": POSITION,
    "submission": SUBMISSION,
    "transition": TRANSITION,
    "entry": ENTRY,
    "action": ACTION,
}

BASE_META_NODE_SETTINGS = {
    "text": TEXT,
    "comment": COMMENT,
}

SCORE_NODE_SETTINGS = [
    dict(v, node_type=f"score-{k}-user", fill_opacity=COMMON_NODE_PROPS["user_opacity"])
    for k, v in BASE_SCORE_NODE_SETTINGS.items()
] + [
    dict(
        v,
        node_type=f"score-{k}-opponent",
        fill_opacity=COMMON_NODE_PROPS["opponent_opacity"],
    )
    for k, v in BASE_SCORE_NODE_SETTINGS.items()
]

META_NODE_SETTINGS = [
    dict(v, node_type=f"meta-{k}") for k, v in BASE_META_NODE_SETTINGS.items()
]

DEFAULT_NODE_SETTINGS = SCORE_NODE_SETTINGS + META_NODE_SETTINGS
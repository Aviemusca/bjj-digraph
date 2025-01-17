from django import forms

from .models import DefaultNodeSettings


class NodeSettingsChangeForm(forms.ModelForm):
    class Meta:
        fields = (
            "node_type",
            "level",
            "shape_id",
            "type_text",
            "fill",
            "fill_opacity",
            "stroke",
            "stroke_opacity",
            "stroke_width",
        )


class SiteSettingsChangeForm(forms.ModelForm):
    class Meta:
        fields = (
            "name",
            "site_url",
        )

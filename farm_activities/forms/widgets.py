import json

from django.core.exceptions import ValidationError
from django import forms
from django.conf import settings
from django.forms import modelform_factory
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.urls import reverse



class ReadOnlyNestedActivitiesWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        # Check if there are any nested activities
        if value:
            actual_value = self.choices.queryset.filter(pk__in=value)
            # Create a Bootstrap-styled list with links
            list_items = [
                f'<li class="list-group-item">'
                f'<a href="{reverse("calendar_activity_edit", kwargs={"pk": act.pk})}" class="text-decoration-none">'
                f'{act}</a></li>'
                for act in actual_value  # Assuming `value` is a queryset of nested activities
            ]

            # Wrap the list items in a Bootstrap unordered list
            return mark_safe(
                f'<ul class="list-group">{"" .join(list_items)}</ul>'
            )
        return mark_safe("<p>No nested activities</p>")


class CompostMaterialsWidget(forms.widgets.Widget):
    template_name = "farm_activities/widgets/compost_materials_widgets.html"

    def __init__(self, attrs=None):
        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        if value is None:
            value = []
        elif isinstance(value, str):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                value = []

        return {
            "widget": {
                "name": name,
                "value": json.dumps(value),
                "attrs": self.build_attrs(attrs),
            }
        }
    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = []
        elif isinstance(value, str):
            try:
                value = json.loads(value)
                if value is None:
                    value = []
            except json.JSONDecodeError:
                value = []

        context = {
            "widget": {"name": name, "value": json.dumps(value)},
        }

        return mark_safe(render_to_string(self.template_name, context))

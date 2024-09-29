from django import template

register = template.Library()

@register.filter
def navbar(obj):
    return f"nav/{obj}.html"



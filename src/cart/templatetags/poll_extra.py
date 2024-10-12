from django import template

register = template.Library()

@register.filter
def navbar(obj):
    return f"nav/{obj}.html"

@register.filter
def times(n=12):
    return range(n)
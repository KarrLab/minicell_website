from django import template
import re

register = template.Library()

@register.filter
def isUrlActive(str, pattern):
    return re.match('^/' + pattern + '/*$', str)

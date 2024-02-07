from django import template


register = template.Library()

@register.filter(name='addcent')
def addcent(value):
    return value + 1000
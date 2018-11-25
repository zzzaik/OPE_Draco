from django import template

register = template.Library()

@register.filter(name = 'custom_tags')
def custom_tags(List, i):
    return List[int(i)]


@register.filter(name='index')
def index(List, i):
    return List[int(i)]
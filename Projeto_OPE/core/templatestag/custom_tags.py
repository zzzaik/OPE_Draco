from django import template

register = template.Library()

register.filter('custom_tags', custom_tags)
@register.filter(name = 'custom_tags')
def custom_tags(List, i):
    return List[int(i)]
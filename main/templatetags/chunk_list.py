from django import template

register = template.Library()


@register.filter(is_safe=True)
def chunk_list(value, chunk_size=3):
    for i in range(0, len(value), chunk_size):
        yield value[i:i + chunk_size]

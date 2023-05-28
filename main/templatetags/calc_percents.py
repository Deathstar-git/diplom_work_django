from django import template

register = template.Library()


@register.simple_tag
def calc_percents(total, value):
    if total != 0:
        return int((value / total) * 100)
    else:
        return 0

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="to_kg")
@stringfilter
def to_kg(value):
    return str(int(value) / 10)


@register.filter(name="to_size")
@stringfilter
def to_size(value):
    value = float(value) / 10
    print(value)
    if value >= 1:
        return str(value) + " m"
    else:
        return str(value * 100) + " cm"


@register.filter(name="next")
@stringfilter
def next(value):
    if value > 898:
        return 1
    else:
        return str(value)


@register.filter(name="back")
@stringfilter
def back(value):
    if value < 1:
        return 898
    else:
        return str(value)

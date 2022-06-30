from django import template
import math

register = template.Library()


@register.filter(name="first_half")
def first_half(values):
    return values[: math.ceil(len(values) / 2)]


@register.filter(name="second_half")
def second_half(values):
    return values[math.ceil(len(values) / 2) :]

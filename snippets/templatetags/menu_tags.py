from django import template
import math

from ..models import SocialIconMenu, NavMenu

register = template.Library()

@register.simple_tag()
def get_social_menu():
    menu = SocialIconMenu.objects.filter().first().social_menu_items.all()
    return menu

@register.simple_tag()
def get_nav_menu():
    menu = NavMenu.objects.filter().first().nav_menu_items.all()
    return menu

@register.filter(name='first_word')
def first_word(string):
    return string.split(' ')[0]
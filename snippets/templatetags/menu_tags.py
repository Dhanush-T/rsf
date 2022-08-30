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

@register.filter(name='dept_short')
def dept_short(string):
    if string == "Architecture":
        return "Arch"
    elif string == "Chemical Engineering":
        return "Chem"
    elif string == "Civil Engineering":
        return "Civil"
    elif string == "Chemistry":
        return "Chem"
    elif string == "Computer Applications":
        return "CA"
    elif string == "Computer Science and Engineering":
        return "CSE"
    elif string == "Electrical and Electronics Engineering":
        return "EEE"
    elif string == "Electronics and Communication Engineering":
        return "ECE"
    elif string == "Humanities and Social Sciences":
        return "HSS"
    elif string == "Instrumentation and Control Engineering":
        return "ICE"
    elif string == "Mechanical Engineering":
        return "Mech"
    elif string == "Metallurgical and Materials Engineering":
        return "Meta"
    elif string == "Physics":
        return "Phy"
    elif string == "Production Engineering":
        return "Prod"
    elif string == "Management Studies":
        return "Mgmt"
    elif string == "Mathematics":
        return "Math"
    elif string == "Energy and Environment":
        return "Env"
    elif string == "CECASE":
        return "CECASE"

@register.filter(name='send_filter_dept')
def send_filter_dept(seminars, dept):
    return seminars.filter(department=dept)

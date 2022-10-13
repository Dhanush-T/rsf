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

@register.filter(name='dept_shorter')
def dept_shorter(words):
    
    output = ""
    for word in words:
        if word == "Architecture":
            output+= "Arch, "
        elif word == "Chemical Engineering":
            output+= "Chem, "
        elif word == "Civil Engineering":
            output+= "Civil, "
        elif word == "Chemistry":
            output+= "Chem, "
        elif word == "Computer Applications":
            output+= "CA, "
        elif word == "Computer Science and Engineering":
            output+= "CSE, "
        elif word == "Electrical and Electronics Engineering":
            output+= "EEE, "
        elif word == "Electronics and Communication Engineering":
            output+= "ECE, "
        elif word == "Humanities and Social Sciences":
            output+= "HSS, "
        elif word == "Instrumentation and Control Engineering":
            output+= "ICE, "
        elif word == "Mechanical Engineering":
            output+= "Mech, "
        elif word == "Metallurgical and Materials Engineering":
            output+= "Meta, "
        elif word == "Physics":
            output+= "Phy, "
        elif word == "Production Engineering":
            output+= "Prod, "
        elif word == "Management Studies":
            output+= "Mgmt, "
        elif word == "Mathematics":
            output+= "Math, "
        elif word == "Energy and Environment":
            output+= "Env, "
        elif word == "CECASE":
            output+= "CECASE, "
    
    return output[:-2]

@register.filter(name='send_filter_dept')
def send_filter_dept(seminars, dept):
    return seminars.filter(department=dept)

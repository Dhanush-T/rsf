from django.utils.html import format_html
from django.templatetags.static import static
from django.contrib.auth.models import Permission
from django.contrib import admin
from researchers.models import ResearcherPage
from wagtail.models import GroupPagePermission

from wagtail.core import hooks


@hooks.register("insert_global_admin_css")
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static("css/theme.css"))


admin.site.register(Permission)
admin.site.register(ResearcherPage)
admin.site.register(GroupPagePermission)
from django.utils.html import format_html
from django.templatetags.static import static

from wagtail.core import hooks
from django.contrib import admin
from django.contrib.auth.models import Permission
from wagtail.models import GroupCollectionPermission, Collection


@hooks.register("insert_global_admin_css")
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static("css/theme.css"))


admin.site.register(Permission)
admin.site.register(GroupCollectionPermission)
admin.site.register(Collection)

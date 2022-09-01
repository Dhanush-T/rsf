from wagtail.models import Collection
from django.utils.html import format_html
from django.templatetags.static import static

from wagtail.core import hooks
from django.contrib import admin
from researchers.models import ResearchesPage, ResearcherPage


@hooks.register("insert_global_admin_css")
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static("css/theme.css"))


admin.site.register(ResearchesPage)
admin.site.register(ResearcherPage)
admin.site.register(Collection)
admin.site.site_header = "RSF Admin"

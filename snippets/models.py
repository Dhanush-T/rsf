from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
)
from wagtail.snippets.models import register_snippet
from wagtail.core.models import Orderable
from modelcluster.models import ClusterableModel



class SocialIconMenuItem(Orderable):
    icon_font_awesome_class_name = models.CharField(max_length=255)
    link_url = models.URLField()

    page = ParentalKey("SocialIconMenu", related_name="social_menu_items")
    panels = [
        FieldPanel("icon_font_awesome_class_name"),
        FieldPanel("link_url"),
    ]


@register_snippet
class SocialIconMenu(ClusterableModel):
    max_count = 1
    panels = [
        InlinePanel("social_menu_items", label="Social Menu Item"),
    ]

class NavMenuItem(Orderable):
    nav_page = models.ForeignKey("wagtailcore.Page", null=True, blank=True, on_delete=models.SET_NULL)
    link_url = models.URLField(null=True, blank=True)
    nav_name = models.CharField(max_length=255, null=True, blank=True)

    page = ParentalKey("NavMenu", related_name="nav_menu_items")
    panels = [
        FieldPanel("nav_page"),
        FieldPanel("link_url"),
        FieldPanel("nav_name")
    ]


@register_snippet
class NavMenu(ClusterableModel):
    max_count = 1
    panels = [
        InlinePanel("nav_menu_items", label="Nav Menu Item"),
    ]

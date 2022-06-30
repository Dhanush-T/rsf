from django.db import models

from django.db import models
from django.db.models.fields import TextField

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel

from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.panels import PageChooserPanel

class TeamPage(Page):

    parent_page_types = [
        "home.HomePage"
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [InlinePanel("people", label="Member")], heading="Team Members"
        )
    ]



class People(Orderable):
    page = ParentalKey(TeamPage, on_delete=models.CASCADE, related_name="people")

    name = models.CharField(max_length=225, blank=False, null=True)
    position = models.CharField(max_length=225, blank=False, null=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    email = TextField(max_length=225, blank=False, null=True)

    phone_number = TextField(max_length=225, blank=True, null=True)

    facebook_link = models.URLField(max_length=225, blank=True, null=True)

    linkedin_link = models.URLField(max_length=225, blank=True, null=True)

    google_scholar_link = models.URLField(max_length=225, blank=True, null=True)

    profile_page = models.ForeignKey(
        "researchers.ResearcherPage",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panel = [
        FieldPanel("name"),
        FieldPanel("position"),
        ImageChooserPanel("image"),
        FieldPanel("email"),
        FieldPanel("phone_number"),
        FieldPanel("facebook_link"),
        FieldPanel("linkedin_link"),
        FieldPanel("google_scholar_link"),
        PageChooserPanel("profile_page", "researchers.ResearcherPage"),
    ]

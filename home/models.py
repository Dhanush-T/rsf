from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel


class CarouselImages(Orderable):

    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    heading = models.CharField(max_length=255, blank=True)
    text = RichTextField(blank=True)

    panels = [
        ImageChooserPanel("carousel_image"),
        FieldPanel("heading"),
        FieldPanel("text"),
    ]


class Events(Orderable):

    title = models.CharField(max_length=255, blank=False, null=True)
    page = ParentalKey("home.HomePage", related_name="events")
    url = models.URLField(blank=False, null=True)
    date_time = models.DateTimeField(blank=False, null=True)
    venue = models.CharField(max_length=255, blank=False, null=True)

    panel = [
        FieldPanel("name"),
        FieldPanel("external_link"),
        FieldPanel("internal_link"),
    ]


class News(Orderable):

    name = models.CharField(max_length=255, blank=False, null=True)
    page = ParentalKey("home.HomePage", related_name="news")
    url = models.URLField(blank=False, null=True)
    panel = [
        FieldPanel("name"),
        FieldPanel("url"),
    ]


class HomePage(Page):

    max_count = 1

    about = RichTextField(blank=False, null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                InlinePanel("carousel_images", min_num=1, label="Image"),
            ],
            heading="Carousel Images",
        ),
        MultiFieldPanel(
            [
                InlinePanel("events", min_num=0, label="Event"),
            ],
            heading="Events",
        ),
        MultiFieldPanel(
            [
                InlinePanel("news", min_num=0, label="News"),
            ],
            heading="News",
        ),
        FieldPanel("about"),
    ]

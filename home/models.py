from django.db import models
import math

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

    side_heading = models.CharField(max_length=255, blank=False, null=True)

    side_text = RichTextField(blank=False, null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("side_heading"),
                FieldPanel("side_text"),
            ],
            heading="Left Side Content",
        ),
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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        all_news = (
            News.objects.filter()
        )
        context["news"] = all_news
        context["newsPageCount"] = range(all_news.count())

        
        all_events = (
            Events.objects.filter().order_by("-date_time")
        )
        context["events"] = all_events
        events_count = all_events.count()
        context["eventsPageCount"] = range(math.ceil(events_count / 4))
        events_rem_count = 0
        if events_count % 4 != 0:
            events_rem_count = math.ceil(4 - events_count % 4)
        context["eventsPageCountRem"] = range(events_rem_count)

        return context

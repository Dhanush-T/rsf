from django.db import models
import math

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from events.models import Event
import datetime


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


class News(Orderable):

    name = models.CharField(max_length=255, blank=False, null=True)
    page = ParentalKey("home.HomePage", related_name="news")
    url = models.URLField(blank=False, null=True)
    description = RichTextField(blank=True)
    panel = [
        FieldPanel("name"),
        FieldPanel("url"),
        FieldPanel("description"),
    ]


class HomePage(Page):

    max_count = 1

    about = RichTextField(blank=False, null=True)

    side_text = RichTextField(blank=False, null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
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
            Event.objects.filter(
                date__gte=datetime.date.today()
            ).order_by("-date")
        )
        context["events"] = all_events
        events_count = all_events.count()
        context["eventsPageCount"] = range(math.ceil(events_count / 4))
        events_rem_count = 0
        if events_count % 4 != 0:
            events_rem_count = math.ceil(4 - events_count % 4)
        context["eventsPageCountRem"] = range(events_rem_count)

        return context

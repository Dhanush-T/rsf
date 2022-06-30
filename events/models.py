import datetime
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel

from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey


class EventsPage(Page):
    parent_page_types = ["home.HomePage"]

    content_panels = Page.content_panels + [
        MultiFieldPanel([InlinePanel("events", label="Event")], heading="Events")
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["events_before_today"] = Event.objects.filter(
            date__lt=datetime.date.today()
        ).order_by("-date")
        context["events_after_today"] = Event.objects.filter(
            date__gte=datetime.date.today()
        ).order_by("-date")

        return context


class Event(Orderable):
    page = ParentalKey("EventsPage", related_name="events")

    name = models.CharField(max_length=255, blank=False, null=False)
    speaker = models.CharField(max_length=255, blank=False, null=False)
    venue = models.CharField(max_length=255, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    time = models.TimeField(blank=False, null=False)
    details = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    registeration_link = models.URLField(max_length=255, blank=True, null=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("speaker"),
        FieldPanel("venue"),
        FieldPanel("date"),
        FieldPanel("time"),
        FieldPanel("details"),
        FieldPanel("registeration_link"),
    ]

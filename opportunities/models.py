import datetime
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel

from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey


class OpportunitiesPage(Page):
    max_count = 1
    parent_page_types = ["home.HomePage"]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [InlinePanel("Opps", label="Opportunities")], heading="Opportunities"
        )
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["Opps_before_today"] = Opp.objects.filter(
            last_date__lt=datetime.date.today()
        ).order_by("-last_date")
        context["Opps_after_today"] = Opp.objects.filter(
            last_date__gte=datetime.date.today()
        ).order_by("-last_date")

        return context


class Opp(Orderable):
    page = ParentalKey("OpportunitiesPage", related_name="Opps")

    name = models.CharField(max_length=255, blank=False, null=False)
    institute = models.CharField(max_length=255, blank=False, null=False)
    department = models.CharField(
        max_length=225,
        blank=False,
        null=False,
        choices=(
            ("Architecture", "Architecture"),
            ("Chemical Engineering", "Chemical Engineering"),
            ("Civil Engineering", "Civil Engineering"),
            ("Chemistry", "Chemistry"),
            ("Computer Applications", "Computer Applications"),
            ("Computer Science and Engineering", "Computer Science and Engineering"),
            (
                "Electrical and Electronics Engineering",
                "Electrical and Electronics Engineering",
            ),
            (
                "Electronics and Communication Engineering",
                "Electronics and Communication Engineering",
            ),
            ("Humanities and Social Sciences", "Humanities and Social Sciences"),
            (
                "Instrumentation and Control Engineering",
                "Instrumentation and Control Engineering",
            ),
            ("Mechanical Engineering", "Mechanical Engineering"),
            (
                "Metallurgical and Materials Engineering",
                "Metallurgical and Materials Engineering",
            ),
            ("Physics", "Physics"),
            ("Production Engineering", "Production Engineering"),
            ("Management Studies", "Management Studies"),
            ("Mathematics", "Mathematics"),
            ("Energy and Environment", "Energy and Environment"),
            ("CECASE", "CECASE"),
        ),
        default="Professor",
    )

    last_date = models.DateField(blank=False, null=False)
    more_details = models.URLField(max_length=255, blank=True, null=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("institute"),
        FieldPanel("department"),
        FieldPanel("last_date"),
        FieldPanel("more_details"),
    ]

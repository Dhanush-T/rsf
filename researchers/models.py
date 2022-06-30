from django.db import models
from django.forms.widgets import Select
from wagtail.admin.forms import WagtailAdminPageForm

from django.db import models
from django.db.models.fields import TextField

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from django.utils.text import slugify


class ResearcherPage(Page):

    parent_page_types = [
        "researchers.ResearchesPage",
    ]

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
        default=None
    )
    bio = RichTextField(blank=False, null=True)
    intrests = RichTextField(blank=False, null=True)
    department = models.CharField(
        max_length=225,
        blank=False,
        null=False,
        choices=(
            ("", ""),
            ("Architecture", "Architecture"),
            ("Chemical Engineering", "Chemical Engineering"),
            ("Civil Engineering", "Civil Engineering"),
            ("Computer Science", "Computer Science"),
            ("Electrical Engineering", "Electrical Engineering"),
            ("Environmental Engineering", "Environmental Engineering"),
            ("Industrial Engineering", "Industrial Engineering"),
            ("Materials Science", "Materials Science"),
            ("Mechanical Engineering", "Mechanical Engineering"),
            ("Nuclear Engineering", "Nuclear Engineering"),
            ("Other", "Other"),
        ),
        default="Professor",
    )

    contact_name = TextField(max_length=225, blank=True, null=True)
    
    phone_number = TextField(max_length=225, blank=True, null=True)
    email = TextField(max_length=225, blank=False, null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel("image"),
                FieldPanel("bio"),
                FieldPanel("intrests"),
                FieldPanel(
                    "department",
                    widget=Select(
                        choices=(
                            ("", ""),
                            ("Architecture", "Architecture"),
                            ("Chemical Engineering", "Chemical Engineering"),
                            ("Civil Engineering", "Civil Engineering"),
                            ("Computer Science", "Computer Science"),
                            ("Electrical Engineering", "Electrical Engineering"),
                            ("Environmental Engineering", "Environmental Engineering"),
                            ("Industrial Engineering", "Industrial Engineering"),
                            ("Materials Science", "Materials Science"),
                            ("Mechanical Engineering", "Mechanical Engineering"),
                            ("Nuclear Engineering", "Nuclear Engineering"),
                            ("Physics", "Physics"),
                        )
                    ),
                ),
            ]
        ),
        MultiFieldPanel(
            [InlinePanel("information", label="information")], heading="Information"
        ),
        MultiFieldPanel(
            [InlinePanel("seminar_and_viva", label="Seminar And Viva Voice")], heading="Seminar And Viva Voice"
        ),
        MultiFieldPanel(
            [
                FieldPanel("contact_name"),
                FieldPanel("phone_number"),
                FieldPanel("email"),
            ],
            heading="Contact",
        ),
    ]

    def clean(self):
        self.title = self.title
        self.slug = slugify(self.title)
        return super().clean()


ResearcherPage._meta.get_field("title").verbose_name = "name"


class Information(Orderable):
    page = ParentalKey("researchers.ResearcherPage", related_name="information")

    title = models.CharField(max_length=225, blank=False, null=True)
    text = RichTextField(
        features=["bold", "italic", "ol", "ul", "link", "document-link"],
        blank=False,
        null=True,
    )

    panels = [FieldPanel("title"), FieldPanel("text")]

class SeminarAndViva(Orderable):
    page = ParentalKey("researchers.ResearcherPage", related_name="seminar_and_viva")

    title = models.CharField(max_length=225, blank=False, null=True)
    
    department = models.CharField(
        max_length=225,
        blank=False,
        null=False,
        choices=(
            ("", ""),
            ("Architecture", "Architecture"),
            ("Chemical Engineering", "Chemical Engineering"),
            ("Civil Engineering", "Civil Engineering"),
            ("Computer Science", "Computer Science"),
            ("Electrical Engineering", "Electrical Engineering"),
            ("Environmental Engineering", "Environmental Engineering"),
            ("Industrial Engineering", "Industrial Engineering"),
            ("Materials Science", "Materials Science"),
            ("Mechanical Engineering", "Mechanical Engineering"),
            ("Nuclear Engineering", "Nuclear Engineering"),
            ("Physics", "Physics"),
        ),
        default="",
    )

    type = models.CharField(
        max_length=225,
        blank=False,
        null=False,
        choices=(
            ("Seminar", "Seminar"),
            ("Viva Voice", "Viva Voice")
        ),
        default="Seminar",
    )

    date = models.DateField(blank=False, null=True)
    time = models.TimeField(blank=False, null=True)
    venue = models.CharField(max_length=225, blank=False, null=True)
    speaker = models.CharField(max_length=225, blank=False, null=True)

    panels = [FieldPanel("title"), FieldPanel("department"), FieldPanel("type"), FieldPanel("date"), FieldPanel("time"), FieldPanel("venue")]

    def save(self, *args, **kwargs):
        self.speaker = self.page.contact_name
        super().save(*args, **kwargs)



class researchersPageWagtailForm(WagtailAdminPageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        title = self.fields["title"]
        title.widget.attrs["value"] = "Researcher"
        slug = self.fields["slug"]
        slug.widget.attrs["value"] = "researcher"


class ResearchesPage(Page):

    subpage_types = [
        "researchers.ResearcherPage",
    ]
    parent_page_types = [
        "home.HomePage",
    ]

    base_form_class = researchersPageWagtailForm

    departments = [
        "",
        "Architecture",
        "Chemical Engineering",
        "Civil Engineering",
        "Computer Science",
        "Electrical Engineering",
        "Environmental Engineering",
        "Industrial Engineering",
        "Materials Science",
        "Mechanical Engineering",
        "Nuclear Engineering",
        "Physics",
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["departments"] = []
        for department in self.departments:
            if ResearcherPage.objects.filter(department=department).count() != 0:
                context["departments"].append(department)
        return context
from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel,
)

from wagtail.core.models import Page

from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtail.core.fields import StreamField
from wagtail.core.blocks import RichTextBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtailmarkdown.blocks import MarkdownBlock

from wagtail.admin.edit_handlers import StreamFieldPanel

from globalPage import blocks

from globalPage.models import new_table_options

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class SingleNewsPage(Page):

    news_title = models.CharField(max_length=100, blank=False, null=True)
    date = models.DateField(blank=False, null=True)
    content = StreamField(
        [
            (
                "table",
                TableBlock(
                    table_options=new_table_options, template="streams/table_block.html"
                ),
            ),
            ("image", ImageChooserBlock()),
            (
                "text",
                RichTextBlock(
                    features=[
                        "h1",
                        "h2",
                        "h3",
                        "h4",
                        "h5",
                        "h6",
                        "bold",
                        "italic",
                        "ol",
                        "ul",
                        "link",
                        "hr",
                        "embed",
                        "document-link",
                        "image",
                        "code",
                        "blockquote",
                        "table",
                        "strikethrough",
                        "superscript",
                        "subscript",
                    ]
                ),
            ),
            ("markdown", MarkdownBlock(icon="code")),
            ("url", blocks.URLBlock(icon="link")),
            ("card", blocks.Card(icon="folder")),
        ],
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("news_title"),
        FieldPanel("date"),
        StreamFieldPanel("content"),
    ]

    subpage_types = []
    parent_page_types = [
        "news.NewsPage",
    ]


class NewsPage(Page):

    news_head = models.CharField(max_length=100, blank=False, null=True)
    news_title = models.CharField(max_length=100, blank=False, null=True)

    subpage_types = [
        "news.SingleNewsPage",
    ]
    parent_page_types = ["home.HomePage"]

    content_panels = Page.content_panels + [
        FieldPanel("news_head"),
        FieldPanel("news_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        circulars_page = NewsPage.objects.first()
        allCirculars = (
            SingleNewsPage.objects.live().child_of(circulars_page).order_by("-date")
        )

        offset = request.GET.get("offset")
        try:
            offset = int(offset)
            paginator = Paginator(allCirculars, offset)
        except:
            paginator = Paginator(allCirculars, 10)
            offset = 10

        page = request.GET.get("page")

        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        context["posts"] = posts
        context["offset"] = offset
        return context

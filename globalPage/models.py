from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import RichTextBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtailmarkdown.blocks import MarkdownBlock

from wagtail.admin.edit_handlers import StreamFieldPanel

from globalPage import blocks

new_table_options = {
    "minSpareRows": 0,
    "startRows": 6,
    "startCols": 4,
    "colHeaders": True,
    "rowHeaders": True,
    "contextMenu": [
        "row_above",
        "row_below",
        "---------",
        "col_left",
        "col_right",
        "---------",
        "remove_row",
        "remove_col",
        "---------",
        "clear_column",
        "undo",
        "redo",
        "---------",
        "copy",
        "cut",
        "---------",
        "alignment",
    ],
}


class GlobalPage(Page):
    """
    This is the Global Page model.
    """

    template = "globalPage/global_page.html"
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
        StreamFieldPanel("content"),
    ]

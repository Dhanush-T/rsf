from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class Card(blocks.StructBlock):

    image = ImageChooserBlock()

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=False, help_text="Add additional text")

    url = blocks.URLBlock(required=False, help_text="Add your url")
    page_link = blocks.PageChooserBlock(required=False, help_text="Add your url")

    open_in_new_tab = blocks.BooleanBlock(required=False, help_text="Open in new tab?")

    class Meta:
        template = "streams/card_block.html"
        icon = "card"
        label = "Card"


class URLBlock(blocks.StructBlock):

    url = blocks.URLBlock(required=True, help_text="Add your url")
    text = blocks.CharBlock(required=True, help_text="Add your url text")

    open_in_new_tab = blocks.BooleanBlock(required=False, help_text="Open in new tab?")

    class Meta:
        template = "streams/url_block.html"
        icon = "link"
        label = "URL"

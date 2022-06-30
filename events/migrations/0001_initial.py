# Generated by Django 4.0.4 on 2022-05-18 08:55

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0069_log_entry_jsonfield"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("event_title", models.CharField(max_length=100, null=True)),
                ("venue", models.CharField(max_length=100, null=True)),
                ("date_time", models.DateTimeField(null=True)),
                (
                    "content",
                    wagtail.fields.StreamField(
                        [
                            (
                                "table",
                                wagtail.contrib.table_block.blocks.TableBlock(
                                    table_options={
                                        "colHeaders": True,
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
                                        "minSpareRows": 0,
                                        "rowHeaders": True,
                                        "startCols": 4,
                                        "startRows": 6,
                                    },
                                    template="streams/table_block.html",
                                ),
                            ),
                            ("image", wagtail.images.blocks.ImageChooserBlock()),
                            (
                                "text",
                                wagtail.blocks.RichTextBlock(
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
                            (
                                "markdown",
                                wagtailmarkdown.blocks.MarkdownBlock(icon="code"),
                            ),
                            (
                                "url",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "url",
                                            wagtail.blocks.URLBlock(
                                                help_text="Add your url", required=True
                                            ),
                                        ),
                                        (
                                            "text",
                                            wagtail.blocks.CharBlock(
                                                help_text="Add your url text",
                                                required=True,
                                            ),
                                        ),
                                        (
                                            "open_in_new_tab",
                                            wagtail.blocks.BooleanBlock(
                                                help_text="Open in new tab?",
                                                required=False,
                                            ),
                                        ),
                                    ],
                                    icon="link",
                                ),
                            ),
                            (
                                "card",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(),
                                        ),
                                        (
                                            "title",
                                            wagtail.blocks.CharBlock(
                                                help_text="Add your title",
                                                required=True,
                                            ),
                                        ),
                                        (
                                            "text",
                                            wagtail.blocks.TextBlock(
                                                help_text="Add additional text",
                                                required=False,
                                            ),
                                        ),
                                        (
                                            "url",
                                            wagtail.blocks.URLBlock(
                                                help_text="Add your url", required=False
                                            ),
                                        ),
                                        (
                                            "page_link",
                                            wagtail.blocks.PageChooserBlock(
                                                help_text="Add your url", required=False
                                            ),
                                        ),
                                        (
                                            "open_in_new_tab",
                                            wagtail.blocks.BooleanBlock(
                                                help_text="Open in new tab?",
                                                required=False,
                                            ),
                                        ),
                                    ],
                                    icon="folder",
                                ),
                            ),
                        ],
                        blank=True,
                        null=True,
                        use_json_field=None,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="EventsPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("events_head", models.CharField(max_length=100, null=True)),
                ("events_title", models.CharField(max_length=100, null=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]

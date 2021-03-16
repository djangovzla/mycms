from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from apps.base.blocks import BaseStreamBlock

class BlogPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full")
    ]

    subpage_types = ["PostPage"]


class PostPage(Page):
    date = models.DateField("Post date")
    summary = models.CharField(max_length=250)
    body = StreamField(
        BaseStreamBlock(),
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("summary"),
        StreamFieldPanel("body"),
    ]

    parent_page_types = ["BlogPage"]


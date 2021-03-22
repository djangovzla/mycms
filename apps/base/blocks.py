from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock


class TitleTextBlock(blocks.StructBlock):
    title_text = blocks.CharBlock(classname="title", required=True)
    size = blocks.ChoiceBlock(
        choices=[
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False
    )

    class Meta:
        icon = "title"
        label = "Title text"
        template = "base/blocks/title_text_block.html"


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    caption = blocks.CharBlock(required=False)

    class Meta:
        icon = "image"
        label = "image"
        template = "base/blocks/image_block.html"


class QuoteBlock(blocks.StructBlock):
    text = blocks.TextBlock(required=True)
    attribute_name = blocks.CharBlock(required=True)

    class Meta:
        icon = "openquote" 
        label = "Quate"
        template = "base/blocks/quote_block.html"



class BaseStreamBlock(blocks.StreamBlock):
    title_text_block = TitleTextBlock()
    image_block = ImageBlock()
    quote_block = QuoteBlock()
    richtext_block = blocks.RichTextBlock(
        icon="edit",
        template="base/blocks/richtext_block.html",
        label="RichText"
    )
    embed_block = EmbedBlock(
        help_text="insert embed",
        label="Embed",
        template="base/blocks/embed_block.html"
    )


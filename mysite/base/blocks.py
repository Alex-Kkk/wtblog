from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageBlock
from wagtail.contrib.table_block.blocks import TableBlock


class CaptionedImageBlock(StructBlock):
    image = ImageBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "base/blocks/captioned_image_block.html"


class HeadingBlock(StructBlock):
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(
        choices=[
            ("", "Select a heading size"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "base/blocks/heading_block.html"

class TableStructBlock(StructBlock):
    table = TableBlock(
        # You can pass optional configurations to the TableBlock constructor
        table_options={
            'minSpareRows': 0,
            'startRows': 5,
            'startCols': 4,
            'colHeaders': True,
            'rowHeaders': True,
            'contextMenu': True,
            'stretchH': 'all',
        },
        help_text="Create and edit your table data here"
    )
    
    class Meta:
        form_classname = 'table'
        icon = "table"
        label = "Table Block"
        #template = "base/blocks/table_block.html"


class BaseStreamBlock(StreamBlock):
    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(icon="pilcrow")
    image_block = CaptionedImageBlock()
    embed_block = EmbedBlock(
        help_text="Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
    )
    table_block = TableBlock()




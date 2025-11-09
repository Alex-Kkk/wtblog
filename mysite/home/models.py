from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class HomePage(Page):
    # add the Hero section of HomePage:
    main_image = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='+'
        )
    intro = models.CharField(
        blank=True,
        max_length=255, help_text="Write an introduction for the site"
    )

    body = RichTextField(blank=True)

    # modify your content_panels:
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("main_image"),
                FieldPanel("intro"),
            ],
            heading="Header section",
        ),
        FieldPanel('body'),
    ]
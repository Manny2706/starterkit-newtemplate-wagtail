
# Create your models here.
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class ProjectPage(Page):
    description = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('description'),
    ]
from django import template

from base.models import FooterText, HomeText

from wagtail.models import Site

register = template.Library()


@register.inclusion_tag("base/includes/footer_text.html", takes_context=True)
def get_footer_text(context):
    footer_text = context.get("footer_text", "")

    if not footer_text:
        instance = FooterText.objects.filter(live=True).first()
        footer_text = instance.body if instance else ""

    return {
        "footer_text": footer_text,
    }

@register.inclusion_tag("base/includes/main_text.html", takes_context=True)
def get_main_text(context):
    main_text = context.get("main_text", "")

    if not main_text:
        instance = HomeText.objects.filter(live=True).first()
        main_text = instance.body if instance else ""

    return {
        "main_text": main_text,
    }

@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page



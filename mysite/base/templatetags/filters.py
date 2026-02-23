from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    """
    Adds a CSS class to a form field (widget).
    Overrides any existing 'class' attribute.
    """
    return value.as_widget(attrs={'class': arg})

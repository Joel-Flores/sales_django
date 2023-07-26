from django import template

from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def render_title(title):
    html = f'<h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300 text-center">{title}</h4>'
    return mark_safe(html)

@register.simple_tag
def render_p(text):
    html = f'<p class="text-lg font-semibold text-gray-700 dark:text-gray-200">{text}</p>'
    return mark_safe(html)

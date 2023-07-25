from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def funtion_p(contex, url, id):
    url = reverse(url, args=[id])
    return mark_safe(f"<p>{contex} con url {url}</p>")
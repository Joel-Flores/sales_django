import json

from django import template
from django.utils.safestring import mark_safe

from .render_button import resolve_url

register = template.Library()

@register.simple_tag
def render_thead(thead):
    list_th = json.loads(thead)
    html = '<tr class="text-xs font-semibold tracking-wide text-left text-gray-500 uppercase border-b dark:border-gray-700 bg-gray-50 dark:text-gray-400 dark:bg-gray-800">'
    for th in list_th:
        html += render_th(th, 'px-4 py-3')
    html += '</tr>'
    return mark_safe(html)

@register.simple_tag
def render_tbody(fields):
    class_ = 'px-4 py-3 text-sm'
    html = str()
    for field in fields:
        url = resolve_url('sales:delete_order', field['id'])
        html += '<tr class="text-gray-700 dark:text-gray-400">'
        html += render_th(field['name'].capitalize(), class_)
        html += render_th(field['count'], class_)
        html += render_th(f"{field['price']} Bs", class_)
        html += render_th(f"{field['total']} Bs", class_)
        html += f''' 
        <td class="px-4 py-3 text-xs">
        <span class="px-2 py-1 font-semibold leading-tight text-red-700 bg-red-100 rounded-full dark:text-red-100 dark:bg-red-700">
            <a href="{url}">Eliminar</a>
        </span>
        </td> '''
        html += '</tr>'
        html += '\n'
    return mark_safe(html)

@register.simple_tag
def render_th(th, class_):
    html = f'<th class="{class_}">{th}</th>'
    return mark_safe(html)
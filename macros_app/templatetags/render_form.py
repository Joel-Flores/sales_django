from django import template

from django.utils.safestring import mark_safe

from .render_text import render_p

from product.helper import HelperProduct

register = template.Library()
      
def render_contex_input(name):
    product = HelperProduct.get_product_name(name)
    
    name = render_p(product.name.capitalize())
    price = render_p(f'{product.price} Bs')
    return name, price

@register.simple_tag
def render_error(error):
    html = f'<li class="text-xs text-red-600 dark:text-red-400">{ error }</li>'
    return mark_safe(html)

@register.simple_tag
def render_input(field, description_input = False):
    html = f''' 
        <div class="text-gray-700 dark:text-gray-400">
            { field.label }
        </div>
        {field}
        '''
    if description_input:
        name, price = render_contex_input(field.name)
        html = f'{name}{price}{html}'
    return mark_safe(html)
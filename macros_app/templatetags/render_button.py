from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def render_button_form(title):
    html = f''' 
    <div class="block mt-4 text-sm">
    <input 
    class="block w-full px-4 py-2 mt-4 text-sm font-medium leading-5 text-center text-white transition-colors duration-150 bg-purple-600 border border-transparent rounded-lg active:bg-purple-600 hover:bg-purple-700 focus:outline-none focus:shadow-outline-purple"
    id="submit" name="submit" type="submit" value="{title}"
    >
    </div>
    '''
    return mark_safe(html)

@register.simple_tag
def render_button(title, url, id = False):
    url = resolve_url(url, id)
    html = f''' 
    <button
    onclick="location.href='{url}'"
    class="flex items-center justify-between w-full px-4 py-2 text-sm font-medium leading-5 text-white transition-colors duration-150 bg-purple-600 border border-transparent rounded-lg active:bg-purple-600 hover:bg-purple-700 focus:outline-none focus:shadow-outline-purple">
      <font style="vertical-align: inherit;">
        <font style="vertical-align: inherit;">
            {title}
        </font>
      </font>
      <span class="ml-2" aria-hidden="true">
        <font style="vertical-align: inherit;">
            <font style="vertical-align: inherit;">+</font>
        </font>
      </span>
    </button>
    '''
    return mark_safe(html)

@register.simple_tag
def render_li(title, url, id=None):
    url = resolve_url(url, id)
    html_a = render_a(title, url)
    html = f'<li class="relative px-6 py-3">{html_a}</li>'
    return mark_safe(html)

@register.simple_tag
def render_a(title, url):
    html = f''' 
    <a class="inline-flex items-center w-full text-sm font-semibold transition-colors duration-150 hover:text-gray-800 dark:hover:text-gray-200" href=" {url} "<svg class="w-5 h-5" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
        <path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path>
        </svg>
        <span class="ml-4">
            <font style="vertical-align: inherit;">
                <font style="vertical-align: inherit;">
                {title}
                </font>
            </font>
        </span>
    </a>
    '''
    return mark_safe(html)

def resolve_url(url, id):
    if id:
        url = reverse(url, args=[id])
    else:
        url = reverse(url)
    return url
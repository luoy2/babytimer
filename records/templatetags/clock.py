from django import template
from django.utils import timezone as tz
register = template.Library()

import datetime

@register.simple_tag
def current_time(format_string):
    return tz.now().strftime(format_string)
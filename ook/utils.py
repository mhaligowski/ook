import os
from django.conf import settings

import pystache

def render_template(template_name, context):
    filepath = os.path.join(settings.MUSTACHE_TEMPLATE_DIR, template_name)
    f = open(filepath, 'r')
    template = f.read()
    f.close()
    
    return pystache.render(template, context)
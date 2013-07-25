# -*- encoding: utf-8 -*-
from pyramid_layout.panel import panel_config

from ..models import SharedURL

@panel_config(name='sharedURLs',
              renderer='panels/shared_urls.mako')
def urls_list(context, request):
    return {'urls': SharedURL.all()}

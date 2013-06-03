# -*- encoding: utf-8 -*-
from pyramid_layout.panel import panel_config

@panel_config(name='footer',
              renderer='panels/footer.mako')
def footer(context, request):
    return {'project_title': "Photo Viewer Express"}

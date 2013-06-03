# -*- encoding: utf-8 -*-
from pyramid.security import (
    remember,
    forget,
    )
from pyramid.httpexceptions import (
    HTTPFound,
    )
from pyramid_layout.panel import panel_config

@panel_config(name='loginbar',
              renderer='panels/loginbar.mako'
              )
def loginbar(context, request):
    return {}


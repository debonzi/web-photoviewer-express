# -*- encoding: utf-8 -*-
from pyramid.security import (
    remember,
    forget,
    )
from pyramid.httpexceptions import (
    HTTPFound,
    )
from pyramid_layout.panel import panel_config

from ..views.users import register_tmpl

@panel_config(name='loginbar',
              renderer='panels/loginbar.mako'
              )
def loginbar(context, request):
    return {}

@panel_config(name='register',
              renderer='panels/register.mako')
def register(context, request):
    return register_tmpl(request)

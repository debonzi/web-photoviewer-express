# -*- encoding: utf-8 -*-
from pyramid.security import (
    remember,
    forget,
    )
from pyramid.httpexceptions import (
    HTTPFound,
    )
from pyramid_layout.panel import panel_config

from ..forms.users import register_tmpl

@panel_config(name='register',
              renderer='panels/base_form.mako')
def register(context, request):
    return register_tmpl(request)


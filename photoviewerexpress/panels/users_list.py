# -*- encoding: utf-8 -*-
from pyramid.security import (
    remember,
    forget,
    )
from pyramid.httpexceptions import (
    HTTPFound,
    )
from pyramid_layout.panel import panel_config

from ..models import Users

@panel_config(name='users_list',
              renderer='panels/users_list.mako')
def users_list(context, request):
    return {'users': Users.all()}

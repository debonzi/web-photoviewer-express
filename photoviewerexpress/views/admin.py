from pyramid.httpexceptions import (
    HTTPFound,
    )

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import (
    DBSession,
    )


@view_config(route_name='admin')
def admin_view(request):
    return HTTPFound(location = request.route_url('photos', directory=""))


@view_config(route_name='admin_register',
             renderer='photoviewerexpress:templates/admin.mako',
             permission='admin')
def admin_register_view(request):
    return {}

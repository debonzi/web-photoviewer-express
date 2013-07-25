from pyramid.httpexceptions import (
    HTTPFound,
    )

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import (
    DBSession,
    )


@view_config(route_name='sharedURLs',
             renderer='photoviewerexpress:templates/sharedURLs.mako',
             permission='admin')
def sharedURLs_view(request):
    return {}

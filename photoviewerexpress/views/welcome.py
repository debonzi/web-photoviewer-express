from pyramid.httpexceptions import (
    HTTPFound,
    )

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import (
    DBSession,
    )


@view_config(route_name='welcome',
             renderer='photoviewerexpress:templates/welcome.mako',
             layout='welcome')
def welcome(request):
    if request.user:
        return HTTPFound(request.route_url('photos', directory=""))
    return {}

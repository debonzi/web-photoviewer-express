from pyramid.httpexceptions import (
    HTTPFound,
    )

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import (
    DBSession,
    )


@view_config(route_name='home')
def home_view(request):
    return HTTPFound(location = request.route_url('photos', directory=""))

import os

from pyramid.httpexceptions import (
    HTTPFound,
    )

from pyramid.response import (
    Response,
    FileResponse
    )
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import (
    DBSession,
    )


@view_config(route_name='favicon')
def favicon_view(request):
    here = os.path.dirname(__file__)
    icon = os.path.join(here, '..', 'static', 'favicon.ico')
    return FileResponse(icon, request=request)

@view_config(route_name='home')
def home_view(request):
    return HTTPFound(location = request.route_url('photos', directory=""))

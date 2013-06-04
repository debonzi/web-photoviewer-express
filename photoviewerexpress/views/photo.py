import os

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPFound,
    )

from sqlalchemy.exc import DBAPIError

from ..models import (
    DBSession,
    )

from ..utils.utils import scan_dir

PHOTOS_PATH = "/home/debonzi/personal/dummydirs"

@view_config(route_name='photos_base')
def photosbase_view(request):
    return HTTPFound(location = request.route_url('photos', directory=""))

@view_config(route_name='photos',
             renderer='photoviewerexpress:templates/photo.mako')
def photos_view(request):
    directory = request.matchdict['directory']
    def files_url(name, url):
        item = dict(
            name=name,
            url=url,
            )
        return item

    dirs_urls = []
    photos_urls = []
    path = ""
    for d in directory:
        path = os.path.join(path, d)

    ##

    dirs, photos = scan_dir(os.path.join(PHOTOS_PATH, path))
    [dirs_urls.append(files_url(d, request.route_url('photos', directory=os.path.join(path,d)))) for d in dirs]
    [photos_urls.append(files_url(f, request.route_url('photos', directory=os.path.join(path,f)))) for f in photos]


    return {'dirs': dirs_urls,
            'photos': photos_urls,
            }

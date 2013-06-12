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

from ..utils.utils import (
    scan_dir,
    get_image_parms,
    get_thumb_parms
    )

# Find a better place for this
PHOTOS_PATH = "/home/debonzi/Pictures"

@view_config(route_name='photos_base')
def photosbase_view(request):
    return HTTPFound(location = request.route_url('photos', directory=""))


@view_config(route_name='photos',
             renderer='photoviewerexpress:templates/photo.mako')
def photos_view(request):
    if not request.user:
        return HTTPFound(request.route_url('welcome'))
    directory = request.matchdict['directory']
    def files_url(name, url, thumb=""):
        item = dict(
            name=name,
            url=url,
            thumb=thumb,
            )
        return item

    dirs_urls = []
    photos_urls = []
    path = ""
    for d in directory:
        path = os.path.join(path, d)

    dirs, photos = scan_dir(os.path.join(PHOTOS_PATH, path))
    [dirs_urls.append(files_url(d, request.route_url('photos', directory=os.path.join(path,d)))) for d in dirs]
    [photos_urls.append(files_url(f,
                                  request.route_url('show', imgpath=os.path.join(path,f)),
                                  request.route_url('showthumb', imgpath=os.path.join(path,f)))) for f in photos]

    return {'dirs': dirs_urls,
            'photos': photos_urls,
            }


@view_config(route_name='show')
def show_image_view(request):
    if not request.user:
        return HTTPFound(request.route_url('welcome'))
    img_path = ""
    for i in request.matchdict['imgpath']:
        img_path = os.path.join(img_path, i)

    fsave, fformat = get_image_parms(os.path.join(PHOTOS_PATH, img_path))
    response = request.response
    response.content_type = 'image/%s'%fformat
    fsave(response.body_file, format=fformat)
    return response

@view_config(route_name='showthumb')
def show_thumb_view(request):
    if not request.user:
        return HTTPFound(request.route_url('welcome'))
    img_path = ""
    for i in request.matchdict['imgpath']:
        img_path = os.path.join(img_path, i)

    fsave, fformat = get_thumb_parms(os.path.join(PHOTOS_PATH, img_path))
    response = request.response
    response.content_type = 'image/%s'%fformat
    fsave(response.body_file, format=fformat)
    return response


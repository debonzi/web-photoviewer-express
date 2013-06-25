import os

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPForbidden,
    )
from pyramid.security import (
    has_permission,
    )

from sqlalchemy.exc import DBAPIError

from ..models import (
    DBSession,
    )

from ..utils.utils import (
    scan_dir,
    scan_root,
    get_image_parms,
    get_thumb_parms
    )

@view_config(route_name='photos_base')
@view_config(route_name='private_root')
@view_config(route_name='public_root')
def photosbase_view(request):
    return HTTPFound(location = request.route_url('photos', directory=""))


@view_config(route_name='photos',
             renderer='photoviewerexpress:templates/photo.mako')
@view_config(route_name='photos_public',
             renderer='photoviewerexpress:templates/photo.mako',
             permission='public')
@view_config(route_name='photos_private',
             renderer='photoviewerexpress:templates/photo.mako',
             permission='private')
def photos_view(request):
    if not request.user:
        return HTTPFound(request.route_url('welcome'))

    route_name = request.matched_route.name
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

    if route_name == "photos_public":
        path = "public"
    elif route_name == "photos_private":
        path = "private"

    for d in directory:
        path = os.path.join(path, d)

    __scan = scan_dir
    if not os.path.basename(path):
        __scan = scan_root

    photos_path = request.registry.settings['photos_path']
    dirs, photos = __scan(photos_path, path,
                          include_private=has_permission('private', request.context, request))

    [dirs_urls.append(files_url(os.path.basename(d),
                                request.route_url('photos', directory=os.path.join(path,d)))) for d in dirs]
    [photos_urls.append(files_url(os.path.basename(f),
                                  request.route_url('show', imgpath=os.path.join(path,f)),
                                  request.route_url('showthumb', imgpath=os.path.join(path,f)))) for f in photos]

    return {'dirs': dirs_urls,
            'photos': photos_urls,
            }


@view_config(route_name='show')
@view_config(route_name='showthumb')
def show_image_view(request):
    if not request.user:
        return HTTPFound(request.route_url('welcome'))
    route_name = request.matched_route.name

    if not has_permission(request.matchdict['imgpath'][0],
                          request.context, request):
        return HTTPForbidden()

    img_path = ""
    for i in request.matchdict['imgpath']:
        img_path = os.path.join(img_path, i)


    if route_name == "show":
        __get_parms = get_image_parms
        res = request.registry.settings['show_resolution']
    elif route_name == "showthumb":
        __get_parms = get_thumb_parms
        res = request.registry.settings['thumb_resolution']

    photos_path = request.registry.settings['photos_path']
    fsave, fformat = __get_parms(os.path.join(photos_path, img_path), res)
    response = request.response
    response.content_type = 'image/%s'%fformat
    fsave(response.body_file, format=fformat)
    return response


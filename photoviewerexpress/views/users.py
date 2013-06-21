# -*- encoding: utf-8 -*-
from pyramid.httpexceptions import HTTPFound

from pyramid.view import view_config


from ..models import DBSession
from ..models import Emails, Users

@view_config(route_name='user_delete',
             permission='admin')
def delete_user(request):
    username = request.matchdict['username'].strip()
    user = Users.by_login(username)
    DBSession.delete(user.emails)
    DBSession.delete(user)
    DBSession.flush()
    return HTTPFound(location = request.route_url('admin', directory=""))

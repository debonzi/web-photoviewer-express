from pyramid.security import (
    remember,
    forget,
    )
from pyramid.httpexceptions import (
    HTTPFound,
    )
from pyramid.view import view_config

from sqlalchemy.exc import IntegrityError

from ..models import DBSession
from ..models import Emails, Users

@view_config(route_name='login')
def login(request):

    login_url = request.route_url('login')
    register_url = request.route_url('register')
    origin_url = request.url
    if (origin_url == login_url or origin_url == register_url):
        origin_url = request.route_url('home')

    if 'form.submitted' in request.params:
        login = request.params['login']
        password = request.params['password']
        user = Users.by_login(login)
        if user and user.validate_password(password):
            headers = remember(request, user.id)
            return HTTPFound(location = origin_url,
                             headers = headers)

        message = 'Failed login'
    return HTTPFound(location = origin_url)


@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = request.route_url('home'),
                     headers = headers)

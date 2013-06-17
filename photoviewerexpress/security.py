from pyramid.security import (
    remember,
    forget,
    authenticated_userid,
    Allow,
    Everyone,
    )

from models import (
    DBSession,
    Users,
    Groups,
    )

class RootFactory(object):
    __acl__ = [(Allow, 'public', 'public'),
               (Allow, 'private', 'public'),
               (Allow, 'private', 'private'),
               (Allow, 'admin', 'public'),
               (Allow, 'admin', 'private'),
               (Allow, 'admin', 'admin')
               ]

    def __init__(self, request):
        pass

def groupfinder(userid, request):
    user = Users.by_id(userid)
    return [g.name for g in user.groups]

def get_user(request):
    userid = authenticated_userid(request)
    if userid is not None:
        return Users.by_id(userid)

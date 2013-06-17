import os
from pyramid_layout.panel import panel_config

@panel_config(name='navbar',
              renderer='panels/navbar.mako'
              )
def navbar(context, request):
    _ = request.translate
    homeurl = request.route_url('home')
    logouturl = request.route_url('logout')
    directory = request.matchdict['directory']

    route_name = request.matched_route.name

    def nav_item(name, url):
        active = request.current_route_url() == url
        item = dict(
            name=name,
            url=url,
            active=active
            )
        return item
    nav = []
    path = ""
    if route_name == "photos_public":
        path = "public"
    elif route_name == "photos_private":
        path = "private"

    for d in directory:
        nav.append(nav_item(d,
                            request.route_url('photos', directory=os.path.join(path,d))))
        path = os.path.join(path, d)

    user_dropdown = [
        nav_item(_(u"Settings"), '#'),
        ]

    return {
        'logouturl': logouturl,
        'homeurl': homeurl,
        'nav': nav,
        'user_dropdown': user_dropdown
        }

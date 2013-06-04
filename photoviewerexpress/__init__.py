from pyramid.config import Configurator

from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from pyramid.i18n import default_locale_negotiator
from .security import groupfinder, get_user


from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    # session factory
    session_factory = UnencryptedCookieSessionFactoryConfig('willneverkn0w')
    config = Configurator(settings=settings,
                          session_factory=session_factory,
                          root_factory='photoviewerexpress:security.RootFactory',
                          locale_negotiator=default_locale_negotiator)

    ## Authorization and Authentication
    authn_policy = AuthTktAuthenticationPolicy(
        'sosecret', callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.add_request_method(get_user, 'user', reify=True)

    ## Localization and Internationalization
    config.add_subscriber('photoviewerexpress.subscribers.add_renderer_globals',
                          'pyramid.events.BeforeRender')
    config.add_subscriber('photoviewerexpress.subscribers.add_localizer',
                          'pyramid.events.ContextFound')
    config.add_translation_dirs('photoviewerexpress:locale')


    ## Static content
    config.add_static_view('static', 'static', cache_max_age=3600)

    ## URL Mapping
    config.add_route('home', '/')
    config.add_route('photos_base', '/photos')
    config.add_route('photos', '/photos/*directory')
    config.scan()
    return config.make_wsgi_app()

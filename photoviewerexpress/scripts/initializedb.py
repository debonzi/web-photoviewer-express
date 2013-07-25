import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from ..models import (
    DBSession,
    Base,
    Groups,
    Emails,
    Users,
    SharedURL,
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

    with transaction.manager:
        group_public = Groups(name="public")
        group_private = Groups(name="private")
        group_admin = Groups(name="admin")
        DBSession.add(group_public)
        DBSession.add(group_private)
        DBSession.add(group_admin)

        email_1 = Emails(email="admin@photoviewer.com")
        DBSession.add(email_1)
        DBSession.flush()

        user_1 = Users(login='admin',
                       firstname='Photo Viewer',
                       lastname='Admin',
                       password='admin',
                       )
        user_1.group = group_admin
        user_1.emails = email_1
        DBSession.add(user_1)

        shared = SharedURL("public/pub2013")
        DBSession.add(shared)

        DBSession.flush()

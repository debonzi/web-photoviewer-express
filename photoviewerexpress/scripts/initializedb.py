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
        group_private = Groups(name="private")
        group_admin = Groups(name="admin")
        DBSession.add(group_private)
        DBSession.add(group_admin)

        email_1 = Emails(email="debonzi@gmail.com")
        DBSession.add(email_1)
        DBSession.flush()

        user_1 = Users(login='debonzi',
                       firstname='Daniel Henrique',
                       lastname='Debonzi',
                       password='debonzi123',
                       )
        user_1.groups.append(group_admin)
        user_1.emails.append(email_1)
        DBSession.add(user_1)

        email_2 = Emails(email="daniel@debonzi.net")
        DBSession.add(email_2)
        DBSession.flush()
        user_2 = Users(login='daniel',
                       firstname='Daniel Henrique',
                       lastname='Debonzi',
                       password='debonzi123',
                       )

        user_2.groups.append(group_private)
        user_2.emails.append(email_2)
        DBSession.add(user_2)
        DBSession.flush()

        email_3 = Emails(email="guest@debonzi.net")
        DBSession.add(email_3)
        DBSession.flush()
        user_3 = Users(login='guest',
                       firstname='Photo Viewer',
                       lastname='Guest',
                       password='guest',
                       )

        user_3.emails.append(email_3)
        DBSession.add(user_3)
        DBSession.flush()
        
        # Exemplo de uso
        # emails = user_2.emails # retorna uma lista de Emails
        # print emails
        # for e in emails:
        #     u = e.users #backref
        #     print u.lastname

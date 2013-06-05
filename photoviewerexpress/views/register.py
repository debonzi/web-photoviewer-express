# -*- encoding: utf-8 -*-
from pyramid.httpexceptions import (
    HTTPFound,
    )
from pyramid.view import view_config

from sqlalchemy.exc import IntegrityError

from ..models import (
    DBSession,
    Emails, 
    Users,
    )

@view_config(route_name='register')
def register(request):
    if request.user:
        # User already logedin
        return HTTPFound(request.route_url('home'))

    if 'form.submitted' in request.params:
        login = request.params['login'].strip()
        password = request.params['password'].strip()
        password_check = request.params['password_check'].strip()
        firstname = request.params['firstname'].strip()
        lastname = request.params['lastname'].strip()
        email = request.params['email'].strip()
        user = Users.by_login(login)
        if not password == password_check:
            # Fazer o tratamento correto informando no form
            # Uma opção é usar o flash
            return {}
        # Criar regexp para validação do email e password
        # Acredito que a validação do email possa ser feita
        # no schem do DB.
        # Verificar melhor opção
        # PS: Twitter bootstrap JS deve ter validação com
        # button disable até o email ser valido

        emaildb = Emails(email = email)
        DBSession.add(emaildb)

        try:
            DBSession.flush()
        except IntegrityError:
            print "Email ja existe!"
            return {}

        userdb = Users(login=login, firstname = firstname,
                       lastname=lastname, password = password)
        userdb.emails.append(emaildb)

        DBSession.add(userdb)
        try:
            DBSession.flush()
        except IntegrityError:
            print "User ja existe!"
            return {}

    return HTTPFound(request.route_url('home'))


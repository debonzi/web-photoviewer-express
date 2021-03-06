# -*- encoding: utf-8 -*-
from pyramid.response import Response

from sqlalchemy.exc import IntegrityError

from ..models import DBSession
from ..models import Emails, Users, Groups

from ..validators import DBUser
from ..validators import DBEmail

import colander
import deform

from deform import ZPTRendererFactory
from deform import Form

from deform.widget import TextInputWidget
from deform.widget import CheckedPasswordWidget

from pkg_resources import resource_filename

def _inline_translate(schema, request):
    for node in schema.children:
        try:
            node.widget.placeholder = request.translate(node.widget.placeholder)
        except:
            pass
        try:
            node.widget.confirm_placeholder = request.translate(node.widget.confirm_placeholder)
        except:
            pass

class AddUserSchema(colander.Schema):
    login = colander.SchemaNode(
             colander.String(),
             validator = DBUser(min = 3, max = 50),
             title = '',
             widget = TextInputWidget(css_class='input-xlarge pull-right',
                                      placeholder = u'Login'),
             name = 'login')
    password = colander.SchemaNode(
             colander.String(),
             validator = colander.Length(min = 5),
             widget = CheckedPasswordWidget(css_class='input-xlarge pull-right',
                                            size = 20, placeholder = u'Password',
                                            confirm_placeholder = u'Check Password'),
             name = 'password')
    name = colander.SchemaNode(
             colander.String(),
             validator = colander.Length(min = 1, max = 120),
             widget = TextInputWidget(css_class='input-xlarge pull-right',
                                      placeholder = u'First Name'),
             name = 'firstname')
    lastname = colander.SchemaNode(
             colander.String(),
             validator = colander.Length(min = 1, max = 120),
             widget = TextInputWidget(css_class='input-xlarge pull-right',
                                      placeholder = u'Last Name'),
             name = 'lastname')
    email = colander.SchemaNode(
             colander.String(),
             validator = DBEmail(),
             widget = TextInputWidget(css_class='input-xlarge pull-right',
                                      placeholder = u'Email'),
             name = 'email')

    group_choices = (('public', 'Public'),
                     ('private', 'Private'),
                     ('admin', 'Admin'))
    group = colander.SchemaNode(
        colander.String(),
        validator = colander.OneOf([x[0] for x in group_choices]),
        widget = deform.widget.RadioChoiceWidget(css_class="", values=group_choices,
                                                 inline=True)
        )

def register_tmpl(request):
    schema = AddUserSchema()
    _inline_translate(schema, request)

    deform_templates = resource_filename('deform', 'templates')
    deform_bootstrap_templates = resource_filename('deform_bootstrap', 'templates')
    custom_templates = resource_filename('photoviewerexpress', 'templates/widgets')
    search_path = (custom_templates, deform_bootstrap_templates, deform_templates)
    renderer = ZPTRendererFactory(search_path)

    def get_RForm():
        return Form(schema, buttons = ('register',), formid = 'form-register',
                    renderer = renderer)
    form = get_RForm()

    if 'register' in request.POST:
        controls = request.POST.items()
        try:
            data = form.validate(controls)
            login = data['login'].strip()
            password = data['password'].strip()
            firstname = data['firstname'].strip()
            lastname = data['lastname'].strip()
            email = data['email'].strip()
            group = data['group'].strip()
            #user = Users.by_login(login)

            emaildb = Emails(email = email)
            groupdb = Groups.by_name(group)
            if not groupdb:
                return {'html_code', form.render()}
            DBSession.add(emaildb)

            try:
                DBSession.flush()
            except IntegrityError:
                return {'html_code', form.render()}

            userdb = Users(login=login, firstname = firstname,
                           lastname=lastname, password = password)
            userdb.group = groupdb
            userdb.emails = emaildb

            DBSession.add(userdb)
            try:
                DBSession.flush()
            except IntegrityError:
                return {'html_code', form.render()}

            user = Users.by_login(login)

        except deform.ValidationFailure, e:
            return {'html_form' : e.render()}
        # Success
        return {'html_form' : get_RForm().render()}
    return {'html_form' : form.render()}


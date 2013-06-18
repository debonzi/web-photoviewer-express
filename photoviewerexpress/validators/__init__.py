import translationstring

import colander

from ..models import Emails
from ..models import Users

_ = translationstring.TranslationStringFactory('PhotoViewerExpress')

class DBEmail(colander.Email):
    def __init__(self, msg=None):
        colander.Email.__init__(self, msg)

    def __call__(self, node, value):
        colander.Email.__call__(self, node, value)

        if Emails.by_email(value):
            self.msg = _('Email already registered!')
            raise colander.Invalid(node, self.msg)

class DBUser(colander.Length):
    def __init__(self, min=None, max=None):
        colander.Length.__init__(self, min, max)

    def __call__(self, node, value):
        colander.Length.__call__(self, node, value)

        if Users.by_login(value):
            existing_err = _('User already registered!')
            raise colander.Invalid(node, existing_err)


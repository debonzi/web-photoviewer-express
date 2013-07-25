import os
from hashlib import sha1

from sqlalchemy import (
    Table,
    Column,
    Integer,
    Text,
    Boolean,
    Sequence,
    ForeignKey,
    )

from sqlalchemy.orm import (
    relationship,
)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Groups(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    
    def __init__(self, name):
        self.name = name

    @classmethod
    def by_name(cls, name):
        return DBSession.query(Groups).filter(Groups.name==name).first()


class Emails(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    email = Column(Text, unique=True, nullable=False)

    def __init__(self, email):
        self.email = email

    @classmethod
    def by_email(cls, email):
        return DBSession.query(Emails).filter(Emails.email==email).first()
    

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), 
                primary_key=True)
    login = Column(Text, unique=True, nullable=False)
    firstname = Column(Text, nullable=False)
    lastname = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    active = Column(Boolean, unique=False, default=True)
    emails = relationship(Emails, uselist=False, backref="users")
    email_id = Column(Integer, ForeignKey('emails.id'))
    group = relationship(Groups, uselist=False, backref="users")
    group_id = Column(Integer, ForeignKey('groups.id'))

    @classmethod
    def by_id(cls, userid):
        return DBSession.query(Users).filter(Users.id==userid).first()

    @classmethod
    def by_login(cls, login):
        return DBSession.query(Users).filter(Users.login==login).first()

    @classmethod
    def all(cls):
        return DBSession.query(Users).all()

    def __init__(self, login, firstname, lastname, password):
        self.login = login
        self.firstname = firstname
        self.lastname = lastname
        self._set_password(password)

    def _set_password(self, password):
        hashed_password = password

        if isinstance(password, unicode):
            password_8bit = password.encode('UTF-8')
        else:
            password_8bit = password

        salt = sha1()
        salt.update(os.urandom(60))
        hash = sha1()
        hash.update(password_8bit + salt.hexdigest())
        hashed_password = salt.hexdigest() + hash.hexdigest()

        if not isinstance(hashed_password, unicode):
            hashed_password = hashed_password.decode('UTF-8')

        self.password = hashed_password

    def validate_password(self, password):
        hashed_pass = sha1()
        hashed_pass.update(password + self.password[:40])
        return self.password[40:] == hashed_pass.hexdigest()


class SharedURL(Base):
    __tablename__ = 'shared_url'
    id = Column(Integer, primary_key=True)
    path = Column(Text, nullable=False)
    token = Column(Text, unique=True, nullable=False)

    def __init__(self, path):
        self.path = path
        self.token = os.urandom(64).encode('hex')

    @classmethod
    def by_token(cls, token):
        return DBSession.query(SharedURL).filter(SharedURL.token==token).first()

    @classmethod
    def all(cls):
        return DBSession.query(SharedURL).all()

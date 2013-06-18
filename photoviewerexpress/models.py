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
    id = Column(Integer, Sequence('group_seq_id'),
                primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(Text, unique=True)
    
    def __init__(self, name):
        self.name = name

    @classmethod
    def by_name(cls, name):
        return DBSession.query(Groups).filter(Groups.name==name).first()


class Emails(Base):
    __tablename__ = 'emails'
    id = Column(Integer, Sequence('emails_seq_id'),
                primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
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
    emails = relationship(Emails, backref="users")
    group = relationship(Groups, uselist=False, backref="users")

    @classmethod
    def by_id(cls, userid):
        return DBSession.query(Users).filter(Users.id==userid).first()

    @classmethod
    def by_login(cls, login):
        return DBSession.query(Users).filter(Users.login==login).first()

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



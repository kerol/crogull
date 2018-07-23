# coding: utf-8
import sqlalchemy
from sqlalchemy import event, inspect, orm
from sqlalchemy.engine.url import make_url
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm.exc import UnmappedClassError
from sqlalchemy.orm.session import Session as SessionBase
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import Column

from crogull_sync.settings import settings


class ModelBase(DeclarativeMeta):
    """ Model metaclass """

    def __init__(cls, name, bases, attrs):
        print(bases)
        print(cls.__mro__)
        super(ModelBase, cls).__init__(name, bases, attrs)


class Model:
    """
    Base class for SQLAlchemy declarative_base cls, do not inherit your model from this,
    your db should be a SQLAlchemy instance
    """

    query_class = None
    query = None


class BaseQuery(orm.Query):
    """
    Custom SQLAlchemy Query
    db.Query
    """

class _QueryProperty(object):
    def __init__(self, sa):
        self.sa = sa

    def __get__(self, obj, _type):
        try:
            mapper = orm.class_mapper(_type)
            if mapper:
                return _type.query_class(mapper, session=self.sa.session())
        except UnmappedClassError:
            return None


class Session(SessionBase):
    " db.session "

    def __init__(self, db, auto_commit=False, auto_flush=True, **options):
        bind = db.engine
        binds = {}
        SessionBase.__init__(self, bind=bind, binds=binds, autocommit=auto_commit, autoflush=auto_flush)


class Database:
    """
    Db for all your model operations
    db.session
    db.Model
    """

    def __init__(self, session_options=None):
        self.Query = BaseQuery
        self.session = self._scoped_session(session_options)
        self.Model = self._make_declarative_base()
        self.Column = Column

    def _scoped_session(self, options):
        if options is None:
            options = {}
        options.setdefault('query_cls', self.Query)
        scope_func = None  # default thread-local scope, otherwise this func should return a thread hash id
        return orm.scoped_session(
            orm.sessionmaker(bind=None, class_=Session, autoflush=True, autocommit=False, expire_on_commit=True,
                             db=self, **options),
            scopefunc=scope_func
        )

    def _make_declarative_base(self):
        metadata = None
        bind = None
        print('model start -------')
        model = declarative_base(
            bind=bind,
            metadata=metadata,
            cls=Model,
            name='Model',
            metaclass=ModelBase,
        )
        print('model created-------')
        model.query_class = self.Query
        model.query = _QueryProperty(self)

        return model

    @property
    def engine(self):
        return self.get_engine()

    def get_engine(self):
        options = settings.db_options
        uri = options['uri']
        engine = create_engine(uri, pool_size=20, max_overflow=0)
        return engine



db = Database()

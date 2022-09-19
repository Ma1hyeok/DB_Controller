from environs import Environ
from sqlalchemy.engine.create import create_engine
from sqlalchemy.orm import sessionmaker



class EngineFactory:
    
    @staticmethod
    def get_db_url(user, password, host , dbname ):
        return f"mysql+pymysql://{user}:{password}@{host}/{dbname}"

    @classmethod
    def create_engine_T3_by(cls, dbname, echo=False):
        dburl = cls.get_db_url(
            Environ.T3_DB_USER
            , Environ.T3_DB_PW
            , Environ.T3_DB_HOST
            , dbname
        )
        engine = create_engine(dburl,echo=echo)
        return engine

    @classmethod
    def create_engine_T3(cls, echo = False):
        dburl = cls.get_db_url(
            Environ.T3_DB_USER
            , Environ.T3_DB_PW
            , Environ.T3_DB_HOST
            , Environ.T3_DB_NAME
        )
        engine = create_engine(dburl, echo = echo)
        return engine

    @classmethod
    def create_engine_DATA_by(cls, dbname, echo=False):
        dburl = cls.get_db_url(
            Environ.DATA_DB_USER
            , Environ.DATA_DB_PW
            , Environ.DATA_DB_HOST
            , dbname
        )
        engine = create_engine(dburl, echo=echo)
        return engine
    
    @classmethod
    def create_engine_DATA(cls, echo = False):
        dburl = cls.get_db_url(
            Environ.DATA_DB_USER
            , Environ.DATA_DB_PW
            , Environ.DATA_DB_HOST
            , Environ.DATA_DB_NAME
        )
        engine = create_engine(dburl, echo = echo)
        return engine


class SessionMaker:
    # 엔진을 session에 연결
    def __init__(self, engine):
        self.engine = engine
        self.Session = SessionMaker(bind=self.engine)

    def __enter__(self):
        return self.Session()


class SessionMaker:
    # 엔진을 session에 연결
    def __init__(self, engine):
        self.engine = engine
        self.Session = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)

    def __enter__(self):
        return self.Session()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.engine.dispose()

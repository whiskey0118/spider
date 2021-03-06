from config import getDbconfig
from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def getEngine():
    conf = getDbconfig()
    connect = "{db_type}+pymysql://{user}:{password}@{host}:{port}/{db_name}".format(db_type = conf["db_type"],user = conf["user"], password = conf["password"],host = conf["host"],port = conf["port"],db_name = conf["db_name"])
    engine =create_engine(connect,encoding='utf-8')
    return engine

engine = getEngine()
metadata = MetaData(engine)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

__all__ = ['engine','metadata','session','Base']

def __init__(self):
    self.metadata = metadata
    self.engine = engine
    self.engine = session
    self.engine = Base
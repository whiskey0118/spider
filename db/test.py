from config import getDbconfig
from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Table, Column, INTEGER, String, Text, TIMESTAMP, DateTime, func)

def getEngine():
    conf = getDbconfig()
    connect = "{db_type}+mysqldb://{user}:{password}@{host}:{port}/{db_name}".format(db_type = conf["db_type"],user = conf["user"], password = conf["password"],host = conf["host"],port = conf["port"],db_name = conf["db_name"])
    # engine =create_engine(connect)
    print(connect)
    return

getEngine()
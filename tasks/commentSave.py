from db.engine import session
from db.model import WeiboComment,User,WeiboData
from sqlalchemy.exc import IntegrityError as SqlalchemyIntegrityError
from pymysql.err import IntegrityError as PymysqlIntegrityError
from sqlalchemy.exc import InvalidRequestError



def add_one(data):
    session.add(data)
    session.commit()

def add_all(datas):
    try:
        session.add_all(datas)
        session.commit()
    except (SqlalchemyIntegrityError, PymysqlIntegrityError, InvalidRequestError):
        for data in datas:
            add_one(data)
from .engine import Base,metadata
from sqlalchemy import (Table, Column, INTEGER, String, Text, TIMESTAMP, DateTime, func)


class User(Base):
    user = Table(
        'user', metadata,
        Column('id', INTEGER, primary_key=True),
        Column('name', String(20)),
    )
    __table__ = user


class Color(Base):
    color = Table(
        'color', metadata,
        Column('id', INTEGER, primary_key=True),
        Column('name', String(20))
    )
    __table__ = color
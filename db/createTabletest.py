from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Table, Column, INTEGER, String, Text, TIMESTAMP, DateTime, func)
from .createEngine import metadata,engine


user = Table(
    'user', metadata,
    Column('id',INTEGER, primary_key=True),
    Column('name', String(20)),
)

color = Table(
    'color', metadata,
    Column('id', INTEGER, primary_key=True),
    Column('name', String(20))
)


metadata.create_all()

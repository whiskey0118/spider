from .engine import Base,metadata
from sqlalchemy import (Table, Column, INTEGER, String, Text, TIMESTAMP, DateTime, func)


class WeiboComment(Base):
    weibo_comment = Table('weibo_comment', metadata,
                          Column("id", INTEGER, primary_key=True, autoincrement=True),
                          Column("comment_id", String(50)),
                          Column("comment_cont", Text),
                          Column("comment_screen_name", Text),
                          Column("weibo_id", String(200)),
                          Column("user_id", String(20)),
                          Column("create_time", String(200)),
                          )
    __table__ = weibo_comment


class User(Base):
    wbuser = Table("wbuser", metadata,
                   Column("id", INTEGER, primary_key=True, autoincrement=True),
                   Column("uid", String(20)),
                   Column("name", String(200), default='', server_default=''),
                   Column("gender", INTEGER, default=0, server_default='0'),
                   Column("birthday", String(200), default='', server_default=''),
                   Column("location", String(100), default='', server_default=''),
                   Column("description", String(500), default='', server_default=''),
                   Column("register_time", String(200), default='', server_default=''),
                   Column("verify_type", INTEGER, default=0, server_default='0'),
                   Column("verify_info", String(2500), default='', server_default=''),
                   Column("follows_num", INTEGER, default=0, server_default='0'),
                   Column("fans_num", INTEGER, default=0, server_default='0'),
                   Column("wb_num", INTEGER, default=0, server_default='0'),
                   Column("level", INTEGER, default=0, server_default='0'),
                   Column("tags", String(500), default='', server_default=''),
                   Column("work_info", String(500), default='', server_default=''),
                   Column("contact_info", String(300), default='', server_default=''),
                   Column("education_info", String(300), default='', server_default=''),
                   Column("head_img", String(500), default='', server_default=''),
                   )
    __table__ = wbuser


class WeiboData(Base):
    weibo_data = Table('weibo_data', metadata,
                       Column("id", INTEGER, primary_key=True, autoincrement=True),
                       Column("weibo_id", String(200)),
                       Column("weibo_cont", Text),
                       Column("weibo_img", String(1000)),
                       Column("weibo_img_path", String(1000), server_default=''),
                       Column("weibo_video", String(1000)),
                       Column("repost_num", INTEGER, default=0, server_default='0'),
                       Column("comment_num", INTEGER, default=0, server_default='0'),
                       Column("praise_num", INTEGER, default=0, server_default='0'),
                       Column("uid", String(20)),
                       Column("is_origin", INTEGER, default=1, server_default='1'),
                       Column("device", String(200), default='', server_default=''),
                       Column("weibo_url", String(300), default='', server_default=''),
                       Column("create_time", String(200)),
                       Column("comment_crawled", INTEGER, default=0, server_default='0'),
                       Column("repost_crawled", INTEGER, default=0, server_default='0'),
                       Column("dialogue_crawled", INTEGER, default=0, server_default='0'),
                       Column("praise_crawled", INTEGER, default=0, server_default='0'),
                       )
    __table__ = weibo_data
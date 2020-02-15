# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/2/15 23:31
# File: service.py
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker

from base.ds.conf_service import ConfService


class DBService(object):
    """
    数据库服务
    """

    def __init__(self):
        self.db_info = ConfService().get_conf('db')
        conn_str = '{}://{}:{}@{}/{}'.format(
            self.db_info['type'],
            self.db_info['user'],
            self.db_info['password'],
            self.db_info['host'],
            self.db_info['db_name'])
        self._db_engine = create_engine(
            conn_str,
            convert_unicode=True,
            echo=True,
            poolclass=QueuePool,
            pool_size=200,
            pool_recycle=100)
        self._session_maker = sessionmaker(bind=self._db_engine)

    def get_db(self):
        """
        获取一个db会话
        :return:
        """
        return self._session_maker()

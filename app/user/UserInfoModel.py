# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/2/16 17:09
# File: UserInfo.py
from base.base.base import BaseModel
from sqlalchemy import Column, Integer, String


class UserInfo(BaseModel):
    __tablename__ = 'user_info'

    name = Column(String(40))
    password = Column(String(40))
    mobile = Column(String(15))
    address = Column(String(100))

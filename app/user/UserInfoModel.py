# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/2/16 17:09
# File: UserInfo.py
from base.base.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean


class UserInfo(BaseModel):
    __tablename__ = 'user_info'

    name = Column(String(40), doc='姓名')
    gender = Column(Boolean, doc='性别')
    password = Column(String(40), doc='密码')
    mobile = Column(String(15), doc='手机号')
    address = Column(String(100), doc='地址')

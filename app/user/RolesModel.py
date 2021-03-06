# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/2/16 18:13
# File: RolesModel.py
from base.base.base import BaseModel
from sqlalchemy import Column, Integer, String


class RolesInfo(BaseModel):
    __tablename__ = 'roles_info'

    name = Column(Integer, doc='权限名称')
    description = Column(String(100), doc='权限描述')

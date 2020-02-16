# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/2/16 18:26
# File: RolesGrant.py

from base.base.base import BaseModel
from sqlalchemy import Column, Integer, String


class RolesGrant(BaseModel):
    __tablename__ = 'roles_grant'

    user_id = Column(Integer, doc='用户ID')
    role_id = Column(Integer, doc='权限ID')

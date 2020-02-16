# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/2/16 18:16
# File: NumberItem.py
from base.base.base import BaseModel
from sqlalchemy import Column, Integer, String


class NumberItem(BaseModel):
    __tablename__ = 'number_item'

    category_id = Column(Integer, doc='编码类别ID')
    number = Column(String(50), doc='编码')
    name = Column(String(50), doc='编码名称')
    description = Column(String(100), doc='描述')

# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/2/16 18:16
# File: NumberItem.py
from base.base.base import BaseModel
from sqlalchemy import Column, Integer, String


class NumberItem(BaseModel):
    __tablename__ = 'number_item'

    category_id = Column(Integer)
    number = Column(String(50))
    name = Column(String(50))
    description = Column(String(100))

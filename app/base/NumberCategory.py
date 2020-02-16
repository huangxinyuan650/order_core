# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/2/16 18:16
# File: NumberCategory.py
from base.base.base import BaseModel
from sqlalchemy import Column, Integer, String


class NumberCategory(BaseModel):
    __tablename__ = 'number_category'

    name = Column(String(50))
    number = Column(String(50))
    category_type = Column(Integer)
    description = Column(String(50))

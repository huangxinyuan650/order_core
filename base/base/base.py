# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/2/15 23:31
# File: base.py
from sqlalchemy.ext.declarative import declarative_base, AbstractConcreteBase
from sqlalchemy import Column, Integer

Base = declarative_base(class_registry={})


class BaseModel(AbstractConcreteBase, Base):
    """
    模型基类
    """

    id = Column(Integer, primary_key=True)
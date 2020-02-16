# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/2/16 18:29
# File: GoodsInfo.py

from base.base.base import BaseModel
from sqlalchemy import Column, Integer, String, Float, DateTime


class GoodsInfo(BaseModel):
    __tablename__ = 'goods_info'

    name = Column(String(50), doc='货物名称')
    description = Column(String(100), doc='货物描述')
    price = Column(Float, doc='货物进价')
    count = Column(Integer, doc='存货量')


class GoodsShowInfo(BaseModel):
    __tablename__ = 'goods_show_info'

    goods_id = Column(Integer, doc='商品ID')
    name = Column(String(50), doc='商品名称')
    description = Column(String(100), doc='商品描述')
    icon = Column(String, doc='商品图片index')
    price = Column(Float, doc='商品价格')
    online_time = Column(DateTime, doc='商品上线时间')
    offline_time = Column(DateTime, doc='商品下架时间')

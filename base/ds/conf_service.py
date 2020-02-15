# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/2/15 23:32
# File: conf_service.py
import json
import os


class ConfService(object):
    """
    配置文件获取服务
    配置文件中描述了默认的db、redis和document地址，配置文件地址为document的base下conf目录下对应名字.conf文件
    document的base为启动docker时刻意挂载的目录，动态启动docker时可指定相关配置文件
    指定docker挂载目录下需要有conf、img、photo、document路径，其中conf下为自定义db、redis等配置文件，其余目录为资源目录
    """

    def __init__(self):
        with open('conf/conf.json', 'rb') as f:
            _conf_info = json.load(f)
            self.info = _conf_info
            self._file_base = _conf_info['document']['base']
            _conf_path = os.path.join(self._file_base, _conf_info['document']['conf'])
            if os.path.exists(_conf_path):
                _conf_list = os.listdir(_conf_path)
                for _conf_name in _conf_list:
                    _list = _conf_name.split('.')
                    if len(_list) == 2 and _list[-1] == 'json':
                        with open(os.path.join(_conf_path, _conf_name), 'rb') as c_f:
                            self.info[_list[0]] = json.load(c_f)
        with open('conf/app_info.json', 'rb') as f:
            self.info['app_info'] = json.load(f)

    def get_conf(self, conf_name=None):
        return self.info[conf_name] if conf_name else self.info

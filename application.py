# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/2/15 23:33
# File: Application.py
import tornado.web
from base.db.service import DBService
import importlib
from base.ds.conf_service import ConfService


class Application(tornado.web.Application):
    """
    程序入口
    """

    def start_test_app(self):
        """
        启动测试服务
        :return:
        """
        _app_info = ConfService().get_conf('app_info')
        _test_app = _app_info['test']
        for _module, _path in _test_app.items():
            _module_info = importlib.import_module(_path+'/TestAppHandler.py')

    def execute(self):
        """
        入口
        :return:
        """
        self.start_test_app()
        db_service = DBService()
        db = db_service.get_db()


if __name__ == '__main__':
    Application().execute()

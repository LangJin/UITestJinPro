# -*- coding:utf-8 -*-
import unittest
from time import sleep
from pages import baidu_pages
from common import pyselenium
from common.log import Log
import config


class Test_index_baidu(unittest.TestCase):
    """百度首页测试"""

    @classmethod
    def setUpClass(cls):
        cls.logger = Log()
        cls.logger.info('############################### START ###############################')
        cls.dr = pyselenium.PySelenium(config.browser)
        cls.dr.max_window()

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
        cls.logger.info('###############################  End  ###############################')

    def test_01_title(self):
        """获取首页title"""
        indexpage = baidu_pages.index_pages(self.dr)
        indexpage.open_index_page()
        title = indexpage.get_index_title()
        print(title)
        self.assertEqual('百度一下，你就知道', title)
        sleep(3)

    def test_02_title(self):
        """获取首页title"""
        indexpage = baidu_pages.index_pages(self.dr)
        indexpage.open_index_page()
        title = indexpage.get_index_title()
        print(title)
        self.assertEqual('s342', title)
        sleep(3)

    def test_00_demo(self):
            """ 此用例成功 """
            for i in range(5):
                with self.subTest(data=i):  # 注意这里subTest的用法
                    self.assertEqual(1+2, 3)

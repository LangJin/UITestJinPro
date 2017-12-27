# -*- coding:utf-8 -*-
'''
说明：放的都是各个页面的元素
'''
from common import basepage


class index_pages(basepage.Page):
    '''百度首页的页面元素'''
    def open_index_page(self):
        """打开百度首页"""
        self.dr.open('http://www.baidu.com')

    def get_index_title(self):
        '''获取title'''
        return self.dr.get_title()

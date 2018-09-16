# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from Meizitu.settings import USER_AGENTS as ua

class MeiZiTuSpiderMiddleware(object):
    """
        给每一个请求随机切换一个User-Agent
    """
    def process_request(self, request, spider):
        if request.url != 'http://mzitu.com/':
            user_agent = random.choice(ua)
            request.headers['User-Agent'] = user_agent
            request.headers['Referer']='http://www.mzitu.com/'
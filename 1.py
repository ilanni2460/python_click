# -*- coding: utf-8 -*-
# !/usr/bin/env python
# 抓取百度搜索结果
import sys
import re
import urllib2

#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup

def search(key):
    search_url = 'http://www.baidu.com/s?wd=key&rsv_bp=0&rsv_spt=3&rsv_n=2&inputT=6391'
    req = urllib2.urlopen(search_url.replace('key', key))
    result = []
    # 循环抓取10页结果进行解析
    for count in range(10):
        html = req.read()
        soup = BeautifulSoup(html)

        file = open("result.txt", 'a')

        content = soup.findAll('table', id=re.compile("\d"))
        num = len(content)

        for i in range(num):
            # 先解析出来内容
            p_str = content[i].find('a')
            # 提取关键字
            if p_str.em:
                str = "".join(p_str.em.string)
            # 提取缩略标题
            patt = re.compile(u"<\/em>(.*?)<\/a>")
            text = re.search(patt, unicode(p_str))
            if text:
                str += text.group(1)
            # 构造字典序列
            # result +=[{str:p_str['href']}]
            file.write(str + u'\n' + unicode(p_str['href']) + u'\n')

        file.close()
        # 解析下一页
        next_page = 'http://www.baidu.com' + soup('a', {'href': True, 'class': 'n'})[0][
            'href']  # search for the next page
        req = urllib2.urlopen(next_page)


if __name__ == '__main__':
    key = raw_input('input key word:')
    search(key)
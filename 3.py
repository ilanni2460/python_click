# coding=utf-8
import urllib2
import string
import urllib
import re


def my_urlencode(str):
    reprStr = repr(str).replace(r'\x', '%')
    return reprStr[1:-1]


def clearTag(text):
    p = re.compile(u'<[^>]+>')
    retval = p.sub("", text)
    return retval


def get_res_list_and_next_page_url(target_url):
    res = urllib2.urlopen(target_url)
    html = res.read()
    content = unicode(html, 'utf-8', 'ignore')

    # 获取res_list
    pattern = re.compile(r'<table.*?class="result".*?>[\s\S]*?</table>')  # 大部分情况
    resList_1 = pattern.findall(html)
    pattern = re.compile(r'<div class="result-op c-container.*?>[\s\S]*?</div>.*?</div>')  # 少数情况
    resList_2 = pattern.findall(html)
    res_lists = resList_1 + resList_2  # 合并搜索结果

    # 获取next_page_url
    pattern = re.compile(r'<p id="page".*?>[\s\S]*</p>')
    m = pattern.search(html)
    next_page_url = ''
    if m:
        t = m.group()
        pattern = re.compile(r'<a href=".*?"')
        mm = pattern.findall(t)
        tt = mm[len(mm) - 1]
        tt = tt[9:len(tt) - 1]
        next_page_url = 'http://www.baidu.com' + tt
    return res_lists, next_page_url


def get_title(div_data):
    pattern = re.compile(r'<a[\s\S]*?>.*?<em>.*?</em>')
    m = pattern.search(div_data)
    if m:
        title = clearTag(m.group(0).decode('utf-8').encode('gb18030'))

    pattern = re.compile(r'</em>.*?</a>')  # 加?号是最小匹配
    m = pattern.search(div_data)
    if m:
        title += clearTag(m.group(0).decode('utf-8').encode('gb18030'))
    return title.strip()


def get_url(div_data):
    pattern = re.compile(r'mu="[\s\S]*?"')
    m = pattern.search(div_data)
    if m:  # mu模式
        url = m.group(0)
        url = url.replace("mu=", "")
        url = url.replace(r'"''"''"', "")
    else:  # href模式
        pattern = re.compile(r'href="[\s\S]*?"')
        mm = pattern.search(div_data)
        if mm:
            url = mm.group(0)
            url = url.replace("href=", "")
            url = url.replace(r'"', "")
    return url


def get_abstract(div_data):
    pattern = re.compile(r'<div class="c-abstract">[\s\S]*?</div>')
    m = pattern.search(div_data)
    if m:  # 普通模式
        abstract = clearTag(m.group(0))
    else:  # 奇怪模式1，貌似是外国网站
        pattern = re.compile(r'<div class="op_url_size".*?</div>')
        mm = pattern.search(div_data)
        if mm:
            abstract = clearTag(mm.group(0))
        else:  # 奇怪模式2，貌似是百科等自己的，反正和别人用的不是一个div class~
            pattern = re.compile(r'<div class="c-span18 c-span-last">[\s\S]*?</p>')
            mmm = pattern.search(div_data)  # 这里用match和search结果不一致
            # match是从字符串的起点开始做匹配，而search是从字符串做任意匹配。
            if mmm:
                abstract = clearTag(mmm.group(0))
            else:
                abstract = "No description!"
                # print i
    return abstract.strip()


if __name__ == "__main__":
    # 初始化
    keyword = raw_input('Please enter the keyword you want to search:')
    url = 'http://www.baidu.com/s?wd=' + my_urlencode(keyword) + '&rsv_bp=0&rsv_spt=3&rsv_n=2&inputT=6391'
    target_urls = []
    target_urls.append(url)

    page_num = 2  # 想多少页就多少页。。只要你有。。

    for cnt in range(page_num):
        print "===============第", cnt + 1, "页==============="

        if target_urls[cnt] == "END_FLAG":
            break

        res_lists, next_page_url = get_res_list_and_next_page_url(target_urls[cnt])

        if next_page_url:  # 考虑没有“下一页”的情况
            target_urls.append(next_page_url)
        else:
            target_urls.append("END_FLAG")

        titles = []
        urls = []
        abstracts = []
        print len(res_lists)
        for index in range(len(res_lists)):
            print "第", index + 1, "个搜索结果..."

            # 获取title
            title = get_title(res_lists[index]).strip()
            titles.append(title)
            print "标题：", title

            # 获取URL
            url = get_url(res_lists[index])
            urls.append(url)
            print "URL：", url

            # 获取描述
            abstract = get_abstract(res_lists[index]).strip()
            abstracts.append(abstract)
            print "概要：", abstract

            print "\r\n\r\n"
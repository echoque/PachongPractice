#!/user/bin/python
# -*- coding: utf-8 -*-
import requests,urllib2,cookielib,random,json
from bs4 import BeautifulSoup
def html_sample(url):
    #url='http://news.sina.com.cn/o/2017-10-24/doc-ifymyyxw4478787.shtml'
    #评论数js
    # '''url='http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fymyyxw4478787\
    # &group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20&jsvar=loader_1508805488653_34193515'''''
    # #尝试去掉url末尾的时间戳
    # url='http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fymyyxw4478787\
    # &group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'

    cookie_support= urllib2.HTTPCookieProcessor(cookielib.CookieJar())
    opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    user_agents = [
                            'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
                            'Opera/9.25 (Windows NT 5.1; U; en)',
                            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
                            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
                            'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
                            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
                            "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
                            ]

    agent = random.choice(user_agents)
    opener.addheaders = [("User-agent",agent),("Accept","*/*"),('Referer',url)]
    res=requests.get(url)
    res.encoding='utf-8'
    htmlsample=res.text
    soup=BeautifulSoup(htmlsample,"html.parser")
    return soup





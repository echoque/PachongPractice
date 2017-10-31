#!/usr/bin/python
# -*- encoding:utf-8 -*-
import requests,json
from bs4 import BeautifulSoup
#得到分页URL
def req(url):
    res=requests.get(url)
    res.encoding='utf-8'
    resdic=res.text.lstrip('  newsloadercallback(').rsplit(');')
    result=json.loads(resdic[0])
    newsdetail=[]
    for en in result['result']['data']:
        newsdetail.append(getNewsDetail(en['url']))
    return newsdetail
#得到新闻的详细信息
def getNewsDetail(newsurl):
    result={}
    res=requests.get(newsurl)
    # print res.content
    res.encoding='utf-8'
    soup=BeautifulSoup(res.content,'html.parser')
    result['title']=soup.select('#artibodyTitle')[0].text
    result['body']=soup.select('#artibody')[0].text
    result['time']=soup.select('.time-source')[0].contents[0].strip()
    result['source']=soup.select('.time-source span a')[0].text
    print result

#使用for循环得到多页链接
def duoye(url):
    for i in range(1,3):
        newurl=url.format(i)
        print newurl

if __name__ == '__main__':
    url='http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&\
    level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page=2&callback=newsloadercallback&_=1508908695130'
    #req(url)
    duoye(url)









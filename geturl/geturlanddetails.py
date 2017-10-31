#!/usr/bin/python
# -*- encoding:utf-8 -*-
from bs4 import BeautifulSoup
from conmon import weiliulanqi
import re
url='https://movie.douban.com/nowplaying/hangzhou/'
soup=weiliulanqi.html_sample(url)
item= soup.select(".list-item")[0]
data= item.contents[1].select('a')[0]
print data['href']
print re.search(r'https://movie.douban.com/subject/(.*)?/?from=playing_poster',data['href']).group(1)


#获取id和电影名称

#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from conmon import weiliulanqi
import re,os

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

#获取URL和ID
url='https://movie.douban.com/nowplaying/hangzhou/'
soup=weiliulanqi.html_sample(url)
item= soup.select(".list-item")[0]
data= item.contents[1].select('a')[0]
# print data['href']
# print re.search(r'https://movie.douban.com/subject/(.*)?/?from=playing_poster',data['href']).group(1)


#获取id和电影名称
# nowplaying_movie = soup.find_all('div', id='nowplaying')
# nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_='list-item')
# print nowplaying_movie
# print nowplaying_movie_list[0]
# print len(nowplaying_movie_list)

#获取评论URL=https://movie.douban.com/subject/25821634/comments?start=20&limit=20&sort=new_score&status=P&percent_type=
#简化URLhttps://movie.douban.com/subject/25821634/comments?start=20&limit=20
commenturl='https://movie.douban.com/subject/25821634/comments?start=20&limit=20'
comsoup=weiliulanqi.html_sample(commenturl)
# print comsoup.select('.comment')
comment_list=[]
#print len(comsoup.select('.comment'))
for comment in comsoup.select('.comment'):
     #print  (comment.select('p')[0].string)
     if comment.select('p')[0].string != '        ':
         #comment_list.append(str(comment.select('p')[0].string).strip())
         #将评论存入文件夹
         # with open(os.getcwd()+'/grep.txt','a') as f:
         #        f.write(comment.select('p')[0].string.strip()+"\n")
        comment_list.append(comment.select('p')[0].string.strip())

#清理评论
#将comment_list LIST转换成字符串
comments = ''
for k in range(len(comment_list)):
    comments = comments + (str(comment_list[k])).strip()
print comments


#去除评论中的标点
pattern = re.compile(r'[\u4e00-\u9fa5]+')
filterdata = re.findall(pattern, comments)
cleaned_comments = ''.join(filterdata)
print cleaned_comments
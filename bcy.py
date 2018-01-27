# coding=utf-8
import os
from bs4 import BeautifulSoup
import requests
import re

url = 'https://bcy.net/coser/detail/129858/1909131'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 '
                  'UBrowser/6.1.2107.204 Safari/537.36'}
html = requests.get(url, headers=header)
soup = BeautifulSoup(html.text, 'lxml')
title = soup.find('h1', class_="js-post-title").text
title = title.replace('\n', '')
print(title)
cn = soup.find_all('a', class_="fz14 blue1")[0]['title']
countP = soup.find_all('div', class_="post__type_l")
#
# count = re.compile(r"[^共].?\d(?=P)").search(countP.find('span').text).group(0)
time = soup.find_all('div', class_='post__type_l')[0].text.replace('\n', '')
time = re.search('(201.*?\d)(?= )', time).group(0)
img_url = soup.find_all('img', class_="detail_std detail_clickable")
x = 0
path = './' + cn + '小图' + str(time) + '/'
if not (os.path.exists(path)):
    os.mkdir(path)
    print('创建文件夹:' + cn + '成功')
print('开始下载图片')
for i in img_url:
    x = x + 1
    src = i.get('src')
    html = requests.get(src, headers=header)
    file_name = title + re.compile('(1.*?\d)(?=/post)').search(src).group(0) + str(x) + ".jpg"
    f = open(path + file_name, 'wb')
    f.write(html.content)
    f.close()
    print(file_name)
print()

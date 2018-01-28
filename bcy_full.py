# coding=utf-8
import requests
import re
from bs4 import BeautifulSoup
import os

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/50.0.2661.102 '
                  'UBrowser/6.1.2107.204 Safari/537.36'}


def getSoup(_url):
    html = requests.get(_url, headers=header)
    soup = BeautifulSoup(html.text, "lxml")
    return soup


def createDir(_path):
    if not (os.path.exists(_path)):
        os.mkdir(_path)
        print('创建文件夹:' + _path + '成功')
        print('开始下载图片')


def download_img(img_urls, _title, _path):
    for (index, x) in enumerate(img_urls):
        img_url = x['src'].replace("/w650", "")
        print(img_url)
        img = requests.get(img_url, headers=header)
        img_name = _title + re.compile('(1.*?\d)(?=/post)').search(img_url).group(0)+"-" + str(index)+".jpg"
        print()
        f = open(_path + img_name, 'wb')
        f.write(img.content)
        print("完成下载"+img_name)
        f.close()


url = 'https://bcy.net/coser/detail/129858/1909131'
my_soup = getSoup(url)
full_img_urls = my_soup.find_all('img', class_='detail_std detail_clickable')
cn = my_soup.find_all('a', class_="fz14 blue1")[0]['title']
time = my_soup.find_all('div', class_='post__type_l')[0].text.replace('\n', '')
time = re.search('(201.*?\d)(?= )', time).group(0)
title = my_soup.h1.text.replace('\n', '')
path = './' + cn + '大图' + str(time) + '/'
createDir(path)
download_img(full_img_urls, title, path)
print("下载完成")

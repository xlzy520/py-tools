# coding=utf-8
from bs4 import BeautifulSoup
import requests
import re
import pymysql

count = 0  # 计算总发布量

db = pymysql.connect('localhost', 'root', '863063', '58tc', charset='utf8')  # 创建数据连接，设置utf8格式，显示中文
cursor = db.cursor()  # 使用cursor()方法获取操作游标
add = '''
      insert into lzy(id,indexInfo,title,type,date,price) VALUES (%s,%s,%s,%s,%s,%s);
   '''
cursor.execute('''delete from lzy''')
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 '
                  'UBrowser/6.1.2107.204 Safari/537.36'}
for x in range(0, 8):
    url = "http://dg.58.com/sou/pn" + str(x) + "/?key=吕振业"
    html = requests.get(url, headers=header)
    soup = BeautifulSoup(html.text, 'lxml')
    soup_wrap = soup.find_all('td', class_='t')
    print("第" + str(x) + "页：")
    for index, t in enumerate(soup_wrap):
        count = 1 + count
        soup_title = t.a['title']
        soup_info = re.sub('\s*', "", t.text)  # 正则匹配空格
        soup_house_type = re.compile('(?<=房产信息-).*?(?=-)').findall(soup_info)[0]  # 正则匹配以XX开头，YY结尾，但不包括XX、YY
        # ，并且懒惰匹配，匹配最近的一个'-'
        soup_price = re.compile('(?<=山-).*[元|月]').findall(soup_info)[0]
        soup_date = "2017-" + re.compile('(?<=[元/月-]-).*').findall(soup_info)[0]
        try:
            cursor.execute(add, (count, index + 1, soup_title, soup_house_type, soup_date, soup_price))
            db.commit()
            print("加入数据库成功！")
        except Exception as e:
            print(e)
            db.rollback()
        print(index + 1, soup_title, "房产类型：" + soup_house_type, soup_price, soup_date)
db.close()
print("共发布" + str(count) + "条信息")

# coding=utf-8
import json
import urllib3
import pymysql
import datetime

header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; MI 5 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043906 Mobile Safari/537.36 '
                  'V1_AND_SQ_7.3.5_776_YYB_D QQ/7.3.5.3385 NetType/WIFI WebP/0.3.0 Pixel/1080',
    'Content - Type': 'application/x-www-form-urlencoded',
    'Cookie':
        'uin=o1017866168;'
        'skey=McTPAnNFys; '
}

params = {'dcapiKey': 'user_rank', 'l5apiKey': 'rank_friends', 'params': {"cmd": 1, "pno": 2, "dtype": 1, "pnum": 20}}


def connectMysql(_database, _datas):
    db = pymysql.connect('localhost', 'root', '863063', _database, charset='utf8')  # 创建数据连接，设置utf8格式，显示中文
    cursor = db.cursor()  # 使用cursor()方法获取操作游标
    add = '''
          insert into qqyundong(icon,name,points,uin,praiseCount,praised,rank,appname,date)
           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);
       '''
    try:
        cursor.execute(add, _datas)
        db.commit()
        print(_datas)
        print("加入数据库成功！")
    except Exception as e:
        print(e)
        db.rollback()


file = './qqyundong.json'

pno_max = 14


def writeFile(_pno, _file, _data):
    fb = open(_file, 'a', encoding='utf8')
    if _pno == 0:
        fb.write("[\n")
    if _pno in range(0, 13):
        fb.write(_data + ",\n")
    if _pno in range(pno_max - 1, pno_max):
        fb.write(_data + "\n")
        fb.write("]")
    fb.close()
    print("写入成功")


g_tk = 744089448
url = 'http://yundong.qq.com/cgi/common_u ser_rank_cmd1?g_tk=' + str(g_tk)
now_date = datetime.datetime.now().date()

for pno in range(0, pno_max):
    postbody = "dcapiKey=user_rank&l5apiKey=rank_friends&params=%7B%22cmd%22%3A1%2C%22pno%22%3A" \
               + str(pno) + "%2C%22dtype%22%3A1%2C%22pnum%22%3A20%7D "
    http = urllib3.PoolManager()
    r = http.request("POST", url, body=postbody, headers=header)
    print(r.data.decode())
    qqyd_dict = json.loads(r.data.decode())  # str转dict
    # qqyd_data_str = str(qqyd_data_dict) # dict转为str
    # qqyd_data_bytes = str.encode(qqyd_data_str) # str转为bytes
    qqyd_bytes = json.dumps(qqyd_dict, indent=2, ensure_ascii=False)  # str转bytes ,indent=2缩进2, ensure_ascii=False中文形式保存
    writeFile(pno, file, qqyd_bytes)
    # for x in (qqyd_dict['data'])['list']:
    #     datas = (x['icon'], x['name'], x['points'], x['uin'], x['praiseCount'], x['praised'], x['rank'], x['appname'],
    #              now_date)
    #     connectMysql('qqyundong', datas)

    # print(qqyd_dict['data'])
    # print(type(qqyd_dict)) # >>>class dict
    # print(type(qqyd_bytes)) # >>>class bytes
    # print(type(r.data)) # >>>class str

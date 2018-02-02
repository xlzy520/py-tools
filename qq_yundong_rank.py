# coding=utf-8
import requests
import re
from bs4 import BeautifulSoup
import os
import urllib3

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,image/sharpp,image/apng,'
              '*/*;q=0.8',
    'Cookie': 'RK=ZZKhLDtBfs; qz_gdt=l76eywrhaaaebad36bzq; qua=V1_AND_SQ_7.3.2.762; sd_userid=18481515956187034; '
              'sd_cookie_crttime=1515956187035; __ls_v__=00___30_40; pgv_info=ssid=s2503830570; pgv_pvid=179351073;'
              'ptisp=cm; ptcz=9c550d0950bd4f20f941a0144bfd1457c9d31b86bd70e41ab569ea798a4e287e; pt2gguin=o1017866168; '
              'pt4_token=MZQoWUWKJeMwsQD2hcmN5XJvM4Mr6AWT4K9q4vNJPO4_; '
              'p_skey=aHhi2HNGRsgbbIP1OO1asdKa0oBTuAJZNlKtXeUjY0c_; '
              ' uin=o1017866168; skey=MTfA0AAhVR; p_uin=o1017866168',
    'Q-Auth': '31045b957cf33acf31e40be2f3e71c5217597676a9729f1b',
    'Q-GUID': '48a57d3ac80ec02f9129aae813b788cb',
    'Q-UA2': 'QV=3&PL=ADR&PR=QQ&PP=com.tencent.mobileqq&PPVN=7.3.5&TBSVC=43603&CO=BK&COVC=043906&PB=GE&VE=GA&DE=PHONE'
             '&CHID '
             '=0&LCID=9422&MO= MI5 &RL=1080*1920&OS=7.0&API=24',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; MI 5 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043906 Mobile Safari/537.36 '
                  'V1_AND_SQ_7.3.5_776_YYB_D '
                  'QQ/7.3.5.3385 NetType/WIFI WebP/0.3.0 Pixel/1080',

}

url = 'https://yundong.qq.com/cgi/common_user_rank_cmd1?g_tk=1210718863&dcapiKey=user_rank&l5apiKey=rank_friends' \
      '&params={"cmd":1,"pno":3,"dtype":1."pnum":20} '


def getSoup(_url):
    html = requests.get(_url, headers=header, verify=False)
    soup = BeautifulSoup(html.text, "lxml")
    return soup


requests.packages.urllib3.disable_warnings()
print(getSoup(url).text)

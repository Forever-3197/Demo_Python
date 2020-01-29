# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 21:32:49 2019

@author: lz

爬王者荣耀壁纸
"""

import urllib.request
import json
import time

def deal_url(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")
    page = urllib.request.urlopen(req)
    html = page.read()
    return html

def deal_html(html):
    html = str(html)
    json_content = html.split('(')[1].split(')')[0]
    obj = json.loads(json_content)
#    for each in obj['List']:
#        print(urllib.request.unquote(each['sProdImgNo_7']))
    for each in obj['List']:
        url = urllib.request.unquote(each['sProdImgNo_8'])
        get_pic(url)
        time.sleep(2)

def get_pic(url):
    url_pic = url.split('jpg')[0] + 'jpg' + '/' + '0'
    filename = "./LOL/LOL" + '\\' + url.split('/')[-2]
    urllib.request.urlretrieve(url_pic, filename, None)

if __name__ == '__main__':
    urls = ['https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=%d&iOrder=0&iSortNumClose=1&jsoncallback=jQuery17104751262946310184_1552744038621&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1552744046535' % (p) for p in range(0,18)]
    for each in urls:
        deal_html(deal_url(each))
        time.sleep(2)
#    urls = ['https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=%d&iOrder=0&iSortNumClose=1&jsoncallback=jQuery17104751262946310184_1552744038621&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1552744046535' % (p) for p in range(16,18)]
#
#    for each in urls:
#        deal_html(deal_url(each))
#        time.sleep(2)
#    deal_html(deal_url(urls[15]))
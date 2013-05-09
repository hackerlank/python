#coding=utf-8
'''
Created on 2013-5-9

@author: tangwsh
'''

import httplib2
import string
import time

def get_url_content(url):
    new_url = url
    print("deal url ", new_url)
    try:
        h = httplib2.Http(timeout=5)
        resp, content = h.request(new_url)
    except Exception,e: 
        print e
        content = ""
    return content

def get_url_sinaweibo(depth):
    #s_depth = depth
    url = "http://weibo.yunyun.com/Weibo.php?q=site%3Aweibo.com%20招商银行&wbts=1" + "&p=" + str(depth)
    #print url
    return get_url_content(url)

def get_url_txweibo(depth):
    #s_depth = depth
    url = "http://weibo.yunyun.com/Weibo.php?q=site%3At.qq.com%20招商银行&wbts=1" + "&p=" + str(depth)
    #print url
    return get_url_content(url)

log_path="/Users/tangwsh/Code/Eclipse/macte/log/"

def get_sinaweibo(depth):
    for i in range (1,depth):
        f=open(log_path + "sinaweibo_" + time.strftime("%Y-%m-%d-%A-%X-%Z", time.localtime()) + ".htm", "w")
        re = get_url_sinaweibo(i)
        print >> f,re
        f.close()
        time.sleep(10)
    return 0

def get_tencentweibo(depth):
    for i in range (1,depth):
        f=open(log_path + "tencentweibo_" + time.strftime("%Y-%m-%d-%A-%X-%Z", time.localtime()) + ".htm", "w")
        re = get_url_txweibo(i)
        print >> f,re
        f.close()
        time.sleep(10)
    return 0

get_sinaweibo(5)
get_tencentweibo(5)





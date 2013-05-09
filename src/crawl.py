'Fetech Web Program'
#coding=GBK

import httplib2 
import time

#chmap将数字转换成字符
chmap = {  
    '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,  
    'x':10,'X':10  
    }  

def ch_to_num(ch):  
    return chmap[ch]      
  
#验证是否为身份证ID
def judge_id(s):  
    #print s
    if (len(s) != 18):
        return False
    #print s
    char_list = list(s)  
    num_list = [ch_to_num(ch) for ch in char_list]  
#   print(num_list)
    sum = 0  
    for ii,n in enumerate(num_list):  
        i = 18-ii  
        weight = 2**(i-1) % 11  
        sum = (sum + n*weight) % 11          
#       print "i=%d,weight=%d,n=%d,sum=%d"%(i,weight,n,sum)       
    return sum==1  

#get url list from file
def judge_card(s):
    if (len(s) == 16):
        return True
    else:
        return False
    

#获取文件file中的所有url，一行一个url
def get_url_list(file):
    try:
        f = open(file,'r')
        url_list = [line.strip('\n') for line in f.readlines()]
        f.close()
    except Exception,e: 
        print e
    return url_list
    
#获取url的内容，以depth参数控制深度  
def get_url_content(url, depth):
    new_url = "http://" + url
    print("deal url ", new_url)
    try:
        h = httplib2.Http(timeout=5)
        resp, content = h.request(new_url)
    except Exception,e: 
        print e
        content = ""
    return content
      
#处理url内容，判断是否为身份证或银行卡号
def deal_url(url):
    s = get_url_content(url, 0)
    #save_to_file("a.txt", s)
    #字符串游标
    index = 0
    #处理步长
    step = 1
    while (index < len(s)):
        num = ""
        #抽取页面中的数字
        if(s[index].isdigit() == True):
            while(s[index].isdigit()):
                num += s[index]
                index += step  
        else:
            index += 1  
        if (judge_id(num)):
            #id, size, url
            print("cerifiction id", num, index, url)
        if (judge_card(num)):
            print("bankcard", num, index, url)
            

#main函数   
url_list = get_url_list("url.txt")
for url in url_list:
# print url
    deal_url(url)
print "done"

    
        
        
        
        
        
        
    
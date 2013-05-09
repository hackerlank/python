'Fetech Web Program'
#coding=GBK

import httplib2 
import time
#carry out

#chmap������ת�����ַ�
chmap = {  
    '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,  
    'x':10,'X':10  
    }  

def ch_to_num(ch):  
    return chmap[ch]      
  
#��֤�Ƿ�Ϊ����֤ID
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

#test for fun
    

#��ȡ�ļ�file�е�����url��һ��һ��url
def get_url_list(file):
    try:
        f = open(file,'r')
        url_list = [line.strip('\n') for line in f.readlines()]
        f.close()
    except Exception,e: 
        print e
    return url_list
    
#��ȡurl�����ݣ���depth������������  
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
      
#����url���ݣ��ж��Ƿ�Ϊ����֤�����п���
def deal_url(url):
    s = get_url_content(url, 0)
    #save_to_file("a.txt", s)
    #�ַ����α�
    index = 0
    #��������
    step = 1
    while (index < len(s)):
        num = ""
        #��ȡҳ���е�����
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
            

#main����   
url_list = get_url_list("url.txt")
for url in url_list:
# print url
    deal_url(url)
print "done"

    
        
        
        
        
        
        
    

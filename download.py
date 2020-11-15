import requests
import json
import sys
import os
from os.path import join
import shutil

with open('token.txt') as f:
	COOKIES={'token': f.read().rstrip()}

def check(r, printhead=True, combinenum=0):
    if printhead:
        if len(r.text)>100:
            print(r, r.text[:97]+'...')
        else:
            print(r, r.text)
    else:
        if combinenum==0:
            print(r)
        else:
            print('\r'+str(r)+'   x '+str(combinenum), end='')
    if r.status_code!=200:
        raise
    return r

pid=sys.argv[1]
dpath=sys.argv[2].rstrip('/')+'/'
tpath=join(dpath, 'text/')
tdpath=join(dpath, 'testdata/')
bpath=join(dpath, 'backup/')
pdfpath=join(tpath, 'description.pdf')

if os.path.exists(dpath):
    shutil.rmtree(dpath)
os.mkdir(dpath)
os.mkdir(tpath)
os.mkdir(tdpath)
os.mkdir(bpath)

with requests.Session() as s:
    for k,v in COOKIES.items():
        s.cookies.set(k,v)
    
    
    r=check(s.get('https://api.oj.nctu.me/problems/{}/'.format(pid)))
    with open(join(bpath, 'text.json'), 'wb') as f:
        f.write(r.content)
    m=json.loads(r.content)['msg']
    gid=str(m['group_id'])
    
    l=['title', 'description', 'input', 'output', 'hint', 'source']
    if m['use_pdf']:
        l=['title', 'source']
        with open(pdfpath, 'wb') as f:
            r=check(s.get('https://api.oj.nctu.me/problems/{}/pdf/'.format(pid)), False)
            f.write(r.content)
    for name in l:
        with open(join(tpath, name+'.txt'), 'w', newline='\n', encoding='utf-8') as f:
            m[name]=m[name].replace('\r', '')
            f.write(m[name])
    
    
    r=check(s.get('https://api.oj.nctu.me/problems/{}/testdata/'.format(pid)))
    with open(join(bpath, 'testdata.json'), 'wb') as f:
        f.write(r.content)
    m=json.loads(r.content)['msg']
    
    l,M=['time_limit', 'memory_limit', 'output_limit', 'score', 'sample'],{}
    for name in l:
        M[name]=[]
    cnt=0
    for i in range(len(m)):
        for name in l:
            M[name]+=[m[i][name]]
        l2=['input', 'output']
        for name in l2:
            with open(join(tdpath, name+str(i+1)+'.txt'), 'wb') as f:
                cnt+=1
                r=check(s.get('https://api.oj.nctu.me/testdata/{}/{}/'.format(m[i]['id'], name)), False, cnt)
                f.write(r.content)
    print()
    for name in l:
        with open(join(dpath, name+'.json'), 'w', newline='\n', encoding='utf-8') as f:
            json.dump(M[name], f)
    
    
    r=check(s.get('https://api.oj.nctu.me/submissions/?group_id={}&count=1000000&page=1'.format(gid)))
    with open(join(bpath, 'submissions.json'), 'wb') as f:
        f.write(r.content)

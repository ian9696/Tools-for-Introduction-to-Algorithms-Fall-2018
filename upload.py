import requests
import json
import sys
import os
from os.path import join

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
pdfpath=join(tpath, 'description.pdf')

with requests.Session() as s:
    for k,v in COOKIES.items():
        s.cookies.set(k,v)
    
    
    form={
        'visible': (None, '0'),
        'group_read': (None, '1'),
        'group_write': (None, '1'),
        'use_pdf': (None, '0'),
    }
    l,M=['title', 'description', 'input', 'output', 'hint', 'source'],{}
    if os.path.exists(pdfpath):
        l=['title', 'source']
        form['use_pdf']=(None, '1')
        form['pdf']=M['pdf']=open(pdfpath, 'rb')
    for name in l:
        M[name]=open(join(tpath, name+'.txt'))
        form[name]=(None, M[name])
    
    r=check(s.put('https://api.oj.nctu.me/problems/{}/'.format(pid), files=form))
    for f in M.values():
        f.close()
    
    
    r=check(s.get('https://api.oj.nctu.me/problems/{}/testdata/'.format(pid)))
    m=json.loads(r.content)['msg']
    cnt=0
    for t in m:
        cnt+=1
        check(s.delete('https://api.oj.nctu.me/testdata/{}/'.format(t['id'])), False, cnt)
    print()
    
    
    l=['time_limit', 'memory_limit', 'output_limit', 'score', 'sample']
    l2=['input', 'output']
    M={}
    for name in l:
        with open(join(dpath, name+'.json')) as f:
            M[name]=json.load(f)
    for name in l2:
        M[name]=[]
        for i in range(len(M[l[0]])):
            M[name]+=[open(join(tdpath, name+str(i+1)+'.txt'), 'r')]
    
    cnt=0
    for i in range(len(M[l[0]])):
        form={
            'problem_id': (None, pid),
            'sample': (None, 'false'),
            'time_limit': (None, '1000'),
            'memory_limit': (None, '262144'),
            'output_limit': (None, '262144'),
            'score': (None, '100')
        }
        cnt+=1
        r=check(s.post('https://api.oj.nctu.me/testdata/', files=form), False, cnt)
        tid=str(json.loads(r.content)['msg']['id'])
        
        form={}
        for name in l:
            form[name]=(None, str(M[name][i]))
        for name in l2:
            form[name]=M[name][i]
        cnt+=1
        r=check(s.put('https://api.oj.nctu.me/testdata/{}/'.format(tid), files=form), False, cnt)

    print()
    for name in l2:
        for f in M[name]:
            f.close()

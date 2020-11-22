import requests
import json
import os

with open('token.txt') as f:
	COOKIES={'token': f.read().rstrip()}

PROBLEMS=[907]

with requests.Session() as ses:
    for k, v in COOKIES.items():
        ses.cookies.set(k, v)
    
    r=ses.get('https://api.oj.nctu.edu.tw/submissions/?group_id=19&count=100000&page=1')
    subs=json.loads(r.content)['msg']['submissions']
    
    l=len(subs)
    print(str(l)+' submissions')
    
    subs=[sub for sub in subs if sub['user_id']==14]
    
    l=len(subs)
    print(str(l)+' submissions')
    
    for sub in subs:
        r=ses.get('https://api.oj.nctu.edu.tw/submissions/' + str(sub['id']) + '/file/')
        with open(str(sub['id'])+'.cpp', 'wb') as f:
            f.write(r.content)
            
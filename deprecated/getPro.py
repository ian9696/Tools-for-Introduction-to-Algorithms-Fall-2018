import requests
import os
import json
import datetime

url='https://api.oj.nctu.me/groups/19/problems/?groupId=19&count=100&page=1'

with open('token.txt', encoding='utf-8') as f:
	COOKIES={'token': f.read().rstrip()}

r=requests.get(url, cookies=COOKIES)
print(r)

if not os.path.exists('log/'):
	os.mkdir('log/')
with open('log/getPro_raw_response.json', 'wb') as f:
	f.write(r.content)
s=json.loads(r.content)
with open('log/getPro_decoded_response.txt', 'w', encoding='utf=8') as f:
	f.write(str(s)+'\n\n'+json.dumps(s, indent='\t'))
s=s['msg']['data']
print('totally '+str(len(s))+' problems')

m={}
for l in s:
	t={}
	t['problem_id']=l['id']
	l=l['title'].split()
	t['title']=' '.join(l[3:-3])
	dt=datetime.datetime.strptime(' '.join(l[-2:]), '%m/%d %H:%M:%S)')
	dt=dt.replace(year=2018 if dt.month in range(9, 13) else 2019)
	t['deadline']=str(dt)
	m[l[1]]=t

with open('problems.json', 'w', encoding='utf-8') as f:
	json.dump(m, f, indent='\t')

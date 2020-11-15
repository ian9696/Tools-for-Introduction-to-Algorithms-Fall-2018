import requests
import os
import json
import datetime

url='https://api.oj.nctu.me/groups/19/users/?groupId=19'

with open('token.txt', encoding='utf-8') as f:
	COOKIES={'token': f.read().rstrip()}

r=requests.get(url, cookies=COOKIES)
print(r)

if not os.path.exists('log/'):
	os.mkdir('log/')
with open('log/getUsr_raw_response.json', 'wb') as f:
	f.write(r.content)
s=json.loads(r.content)
with open('log/getUsr_decoded_response.txt', 'w', encoding='utf=8') as f:
	f.write(str(s)+'\n\n'+json.dumps(s, indent='\t'))
s=s['msg']
print('totally '+str(len(s))+' users')

for x in s:
	del x['powers']

with open('users.json', 'w', encoding='utf-8') as f:
	json.dump(s, f, indent='\t')

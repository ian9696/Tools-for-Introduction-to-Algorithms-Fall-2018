import json
import datetime
import re

pa=re.compile(r'^0\d{6}$')

l=['submissions', 'problems', 'users', 'ids', 'ignored_submissions']
for s in l:
	with open(s+'.json', encoding='utf-8') as f:
		vars()[s]=json.load(f)

scores={}
for x in ids:
	scores[x]={}
	for k in problems:
		scores[x][k]=0

cnt,cntpos,cntign=0,0,0
for s in submissions:
	for k,v in problems.items():
		pd=datetime.datetime.strptime(v['deadline'], '%Y-%m-%d %H:%M:%S')
		sd=datetime.datetime.strptime(s['created_at'], '%Y-%m-%d %H:%M:%S')
		if v['problem_id']==s['problem_id']:
			ok=pd>=sd
			p=k
			break
	if not ok:
		continue
	
	for x in users:
		if x['id']==s['user_id']:
			user_id=x['name']
			break
	if user_id not in ids:
		continue
	
	cnt+=1
	if s['score']>0:
		cntpos+=1
	if s['id'] in ignored_submissions:
		cntign+=1
		continue
	scores[user_id][p]=max(scores[user_id][p], s['score'])

print('processed {} submissions, {} problems, {} OJ users, {} registered students, {} ignored submissions'.format(len(submissions), len(problems), len(users), len(ids), len(ignored_submissions)))
print('totally '+str(cnt)+' in time&registered student submissions')
print('totally '+str(cntpos)+' in time&registered student&positive score submissions')
print('ignored '+str(cntign)+' in time&registered student submissions')
with open('scores.json', 'w', encoding='utf-8') as f:
	json.dump(scores, f, indent='\t')

cnt,cnt2=0,0
with open('1071.1205 Grades-20181115_1705-comma_separated.csv', encoding='utf-8') as inp:
	with open('1071.1205 Grades-20181115_1705-comma_separated_output.csv', 'w', encoding='utf-8') as out:
		for l in inp:
			l=l.replace('\n', '')
			if l.count(',')!=19:
				raise
			l=l.split(',')
			if not pa.match(l[2]):
				cnt+=1
			else:
				cnt2+=1
				for i in range(6, 6+13):
					l[i]=str(scores[l[2]][str(i-5)])
			l=','.join(l)
			print(l, file=out)

if cnt!=1 or cnt2!=77:
	raise
print('{} out of {} lines are valid'.format(cnt2, cnt+cnt2))

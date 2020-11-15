import re
import json

pa=re.compile(r'^0\d{6}$')

ids=[]
with open('grades.csv', encoding='utf-8') as inp:
	with open('ids.json', 'w', encoding='utf-8') as out:
		for l in inp:
			if(len(l)<7):
				continue
			l=l.replace('\n', '').split(',')
			if not pa.match(l[2]):
				continue
			ids+=[l[2]]
		json.dump(ids, out, indent='\t')

print('totally '+str(len(ids))+' ids')

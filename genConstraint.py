import json
import os

n=0
for i in range(1, 101):
    if not os.path.exists('testdata/input{}.txt'.format(i)):
        break
    n=i

with open('time_limit.json', 'w', newline='\n', encoding='utf-8') as f:
    json.dump([500]*n, f)
with open('memory_limit.json', 'w', newline='\n', encoding='utf-8') as f:
    json.dump([262144]*n, f)
with open('output_limit.json', 'w', newline='\n', encoding='utf-8') as f:
    json.dump([262144]*n, f)
with open('sample.json', 'w', newline='\n', encoding='utf-8') as f:
    json.dump([False]*n, f)
with open('score.json', 'w', newline='\n', encoding='utf-8') as f:
    json.dump([100]*n, f)

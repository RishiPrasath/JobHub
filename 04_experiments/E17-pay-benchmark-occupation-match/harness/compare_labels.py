import json
from pathlib import Path
E=Path(__file__).resolve().parents[1]
A={a['id']:a for a in json.load(open(E/'data/labels_A.json'))}
B={b['id']:b for b in json.load(open(E/'data/labels_B.json'))}
P={p['id']:p for p in json.load(open(E/'data/postings.json'))}
names={l.split('|')[0]:l.split('|')[1] for l in open(E.parent/'E10-market-value-and-red-flag-experiments/outputs/x3/occupation_names.txt',encoding='utf-8').read().split('\n') if '|' in l}
names['NONE']='NONE'
agree=0;rows=[]
for i in A:
    a,b=A[i],B[i]
    sa={a['primary']}|set(a['alt']); sb={b['code']}|set(b.get('alt',[]))
    strict=a['primary']==b['code']
    ok = strict or (a['primary'] in sb) or (b['code'] in sa)
    agree+=strict
    if not strict:
        rows.append((i,P[i]['title'][:50],a['primary'],names.get(a['primary'],'')[:30],b['code'],names.get(b['code'],'')[:30],'overlap' if ok else 'DISAGREE'))
print('strict primary agreement',agree,'/',len(A))
for r in rows: print(r)

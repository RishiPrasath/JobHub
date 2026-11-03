import sqlite3, random, collections
from pipeline import acra
DB='/data/acra.sqlite'
random.seed(11)
c=sqlite3.connect(DB)
rows=c.execute("select uen,name from ent where lower(status) like 'live%' and type like '%COMPANY%' and rowid % 887 = 0").fetchall()
cand=[(u,n) for u,n in rows if len(acra.toks(n))>=3]
random.shuffle(cand); cand=cand[:300]
res=collections.Counter(); wrong=[]; ok=legit=former=0
for uen,name in cand:
    t=acra.toks(name); q=' '.join(t[:-1])
    r=acra.resolve(DB,q); st=r['state']; res[st]+=1
    ch=(r['chosen'] or {}).get('uen')
    if st in ('exact','likely'):
        row=c.execute("select uen,name,f1,f2,f3 from ent where uen=?",(ch,)).fetchone()
        if ch==uen: ok+=1
        elif acra.toks(row[1])==t[:-1]: legit+=1
        elif any(n and acra.toks(n)==t[:-1] for n in row[2:5]): former+=1
        else: wrong.append((q,name,row[1],st))
print('n',len(cand),dict(res))
print('auto-accepted',res['exact']+res['likely'],'| original entity',ok,'| other entity with exactly that name',legit,'| via former/alternate name',former,'| truly wrong',len(wrong))
for w in wrong[:8]: print('  WRONG',w)

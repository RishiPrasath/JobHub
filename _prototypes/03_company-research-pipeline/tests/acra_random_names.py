import sqlite3, random, re, json, collections
from pipeline import acra
DB='/data/acra.sqlite'
random.seed(7)
c=sqlite3.connect(DB)
rows=c.execute("select uen,name from ent where lower(status) like 'live%' and type like '%COMPANY%' and rowid % 997 = 0").fetchall()
random.shuffle(rows); rows=rows[:300]
def employer_style(n):
    # how a job board might print the name: drop suffix, or keep it, or title case
    m=random.choice([0,1,2])
    if m==0: return re.sub(r'\s*(PTE\.?\s*LTD\.?|PRIVATE LIMITED|LIMITED|LTD\.?)\s*$','',n,flags=re.I).strip()
    if m==1: return n.title()
    return n
res=collections.Counter(); wrong=[]; right_exact=0
for uen,name in rows:
    q=employer_style(name)
    r=acra.resolve(DB,q)
    st=r['state']; res[st]+=1
    ch=(r['chosen'] or {}).get('uen')
    if st in ('exact','likely') :
        if ch==uen: right_exact+=1
        else: wrong.append((q,name,r['chosen']['name'],st))
print('n',len(rows),dict(res))
print('auto-accepted (exact/likely):',res['exact']+res['likely'],'correct uen:',right_exact,'WRONG:',len(wrong))
for w in wrong[:12]: print('  WRONG',w)

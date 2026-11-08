import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const parts=fs.readdirSync(path.join(here,'contributions')).filter(f=>f.endsWith('.json')).map(f=>JSON.parse(fs.readFileSync(path.join(here,'contributions',f),'utf8')));
const q=parts.flatMap(p=>p.queries||[]),i=parts.flatMap(p=>p.inspections||[]),s=parts.flatMap(p=>p.sources||[]),o=parts.flatMap(p=>p.observations||[]);
assert.equal(q.length,66);assert(i.length<=160);assert.equal(new Set(q.map(x=>x.id)).size,q.length);
assert(q.every(x=>x.query&&x.venue&&x.date&&!/planned|pending/i.test(x.status)),'Unexecuted query counted');
const ids=new Set(s.map(x=>x.id));
for(const x of o)for(const id of x.sourceIds||[])assert(ids.has(id),'Unresolved observation source '+id);
for(const x of q)for(const id of x.sourceIds||[])assert(ids.has(id),'Unresolved query source '+id);
const profiles=JSON.parse(fs.readFileSync(path.join(here,'industry-profiles/profiles.json'),'utf8'));
assert.equal(profiles.length,13);assert.equal(new Set(profiles.map(x=>x.id)).size,13);
const deep=profiles.filter(x=>x.depth==='selected deep dive');
assert.equal(deep.length,6);assert(deep.every(x=>x.id!=='S12'),'Expected six non-IT deep dives');
for(const p of profiles){assert(fs.existsSync(path.join(here,'industry-profiles',p.id+'.md')));for(const id of p.sourceIds)assert(ids.has(id),'Unknown profile source '+id);}
for(const p of deep){const body=fs.readFileSync(path.join(here,'sectors',p.id+'.md'),'utf8');assert.equal([...body.matchAll(/^## [1-9]\./gm)].length,9,'Missing deep-profile sections '+p.id);}
function walk(dir){return fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(dir,e.name)):[path.join(dir,e.name)]);}
const files=walk(here),errors=[];let links=0;
for(const file of files.filter(x=>x.endsWith('.md'))){
  const text=fs.readFileSync(file,'utf8');
  for(const m of text.matchAll(/\]\(([^)]+)\)/g)){
    const target=m[1].replace(/^<|>$/g,'');
    if(/^(https?:|mailto:|#)/.test(target))continue;
    links++;if(!fs.existsSync(path.resolve(path.dirname(file),target.split('#')[0])))errors.push(path.basename(file)+': '+target);
  }
  for(const m of text.matchAll(/\bR3-[A-Z]\d{2}\b/g))if(!ids.has(m[0]))errors.push(path.basename(file)+': unknown source '+m[0]);
}
assert.deepEqual(errors,[]);
const summary={checkedAt:new Date().toISOString(),scope:'Local records, arithmetic, structure, references and file presence only; not independent web-source validation',queries:q.length,inspectionAttempts:i.length,contributedSourceRows:s.length,uniqueSourceIds:ids.size,observations:o.length,profiles:profiles.length,nonITDeepDives:deep.length,localLinks:links,files:files.filter(f=>!f.endsWith('research-validation.json')).map(f=>({path:path.relative(here,f).replaceAll('\\','/'),sha256:crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex')}))};
fs.writeFileSync(path.join(here,'research-validation.json'),JSON.stringify(summary,null,2));
console.log(JSON.stringify({...summary,files:summary.files.length}));

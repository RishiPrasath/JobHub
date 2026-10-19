// Mechanical coordinator merge. Authored conclusions live in the Markdown reports.
import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const dir=path.join(here,'contributions');
const files=fs.readdirSync(dir).filter(x=>x.endsWith('.json')).sort();
const parts=files.map(file=>({file,...JSON.parse(fs.readFileSync(path.join(dir,file),'utf8'))}));
const queries=parts.flatMap(p=>(p.queries||[]).map(x=>({...x,worker:p.worker})));
const inspections=parts.flatMap(p=>(p.inspections||[]).map(x=>({...x,worker:p.worker})));
const sourceRows=parts.flatMap(p=>(p.sources||[]).map(x=>({...x,worker:p.worker,contribution:p.file})));
const sourceMap=new Map();
for(const s of sourceRows){
  if(!sourceMap.has(s.id)){sourceMap.set(s.id,{...s,contributions:[s.contribution]});continue;}
  const prior=sourceMap.get(s.id);
  assert.equal(prior.url.replace(/\/$/,''),s.url.replace(/\/$/,''),'Conflicting URL for reused source '+s.id);
  prior.contributions.push(s.contribution);
  for(const [k,v] of Object.entries(s)){
    if(v && (!prior[k] || /^unknown/i.test(strValue(prior[k]))) && !/^unknown/i.test(strValue(v)))prior[k]=v;
  }
}
function strValue(x){return typeof x==='string'?x:JSON.stringify(x);}
const sources=[...sourceMap.values()];
const observations=parts.flatMap(p=>(p.observations||[]).map(x=>({...x,worker:p.worker})));
for(const [name,rows] of [['query',queries],['source',sources],['observation',observations]]){
  assert.equal(new Set(rows.map(x=>x.id)).size,rows.length,'Duplicate '+name+' IDs');
}
assert(queries.length<=66,'Query ceiling exceeded');
assert(inspections.length<=160,'Inspection ceiling exceeded');
const sourceIds=new Set(sources.map(x=>x.id));
for(const o of observations)for(const id of o.sourceIds||[])assert(sourceIds.has(id),'Unknown observation source '+id);
const str=x=>x===undefined||x===null?'unknown':typeof x==='string'?x:JSON.stringify(x);
const cell=x=>str(x).replaceAll('|','/').replaceAll('\n',' ');
const table=(headers,rows)=>['| '+headers.join(' | ')+' |','| '+headers.map(()=>'---').join(' | ')+' |',...rows.map(r=>'| '+r.map(cell).join(' | ')+' |')].join('\n');
const write=(file,body)=>fs.writeFileSync(path.join(here,file),body+'\n');
write('query-log.md','# Round 03 executed query and inspection log\n\nAccess date: 2026-10-19, Asia/Singapore. Exact submitted strings, including failed searches, come from worker contributions. No search count is a prevalence or confidence measure. Individual wall-clock timestamps were not captured consistently; the day is retained rather than invented precision. Source IDs in a batched breadth search are basket-routing links, not proof of which single string returned each result.\n\nExecuted queries: '+queries.length+'/66. Source-inspection attempts: '+inspections.length+'/160.\n\n## Search attempts\n\n'+table(['ID','Worker','Exact query','Purpose','Status/result','Sources'],queries.map(x=>[x.id,x.worker,x.query,x.intent,x.status+'; '+str(x.resultNote),x.sourceIds||[]]))+'\n\n## Source-inspection attempts\n\n'+table(['Attempt','Worker','URL/resource','Status','Note'],inspections.map((x,i)=>[i+1,x.worker,x.url||x.ref||'not recorded',x.status,x.note||x.result||'unknown']))+'\n\n## Original contributions\n\n'+parts.map(p=>'- ['+p.file+'](contributions/'+p.file+')').join('\n'));
const families=new Map();
write('source-context-fields.md','# Source comparison fields\n\nThese are source-specific contexts, not population strata. Unknown stays unknown. Reused source IDs retain one origin and link all original contributions. Page updates are not publication or event dates.\n\n'+table(['ID','Employer activity','Occupation','Arrangement','Intermediary/client','Stage','Publication / update / event'],sources.map(s=>[s.id,s.employerActivity||'unknown',s.occupation||'unknown',s.arrangement||'unknown',str(s.intermediary||'unknown')+' / '+str(s.clientWorksite||'unknown'),s.stage||'unknown',str(s.publicationDate)+' / '+str(s.updateDate||'unknown')+' / '+str(s.eventPeriod)])));
function canonical(url){try{const u=new URL(url);u.search='';u.hash='';return u.href.replace(/\/$/,'');}catch{return url;}}
for(const s of sources){s.canonicalUrl=canonical(s.url);const key=s.canonicalUrl;if(!families.has(key))families.set(key,[]);families.get(key).push(s.id);}
write('sources.md','# Round 03 inspected sources\n\nAccess date: 2026-10-19. Retained records: '+sources.length+'. Unique canonical URLs: '+families.size+'. Neither is an independent participant/sample size. Same-URL records below are aliases, not corroboration. Different URLs can still share a platform, study, employer statement or story family. See contribution records for original family labels and methods.\n\n'+sources.map(s=>'## '+s.id+': '+s.title+'\n\n- Original: '+s.url+'\n- Publisher/type: '+str(s.publisher)+'; '+str(s.type)+'\n- Geography/tags: '+str(s.geography)+'; '+str(s.tags)+'\n- Publication: '+str(s.publicationDate)+'; underlying period: '+str(s.eventPeriod)+'; access: '+str(s.accessDate)+'\n- Family: '+str(s.family)+'; same-URL IDs: '+families.get(s.canonicalUrl).join(', ')+'\n- Method: '+str(s.method)+'\n- Inspected location/paraphrase: '+str(s.passage)+'\n- Observation: '+str(s.observation)+'\n- Label/confidence: '+str(s.claimLabel)+'; '+str(s.confidence)+'\n- Limits: '+str(s.limits)).join('\n\n'));
write('observations.md','# Round 03 source-linked observations\n\nThese are attributed observations before integration. Confidence is not representativeness. Source-reported experience is not directly observed behaviour.\n\n'+observations.map(o=>'## '+o.id+'\n\n'+str(o.text)+'\n\nSources: '+str(o.sourceIds)+'. Label: '+str(o.label)+'. Limits: '+str(o.limits)).join('\n\n'));
write('register-summary.json',JSON.stringify({date:'2026-10-19',contributions:parts.map(x=>x.file),queries:queries.length,inspections:inspections.length,sourceRecords:sources.length,canonicalUrls:families.size,observations:observations.length,queryRemaining:66-queries.length,inspectionRemaining:160-inspections.length,duplicates:[...families].filter(([,ids])=>ids.length>1)},null,2));
console.log(JSON.stringify({contributions:files,queries:queries.length,inspections:inspections.length,sources:sources.length,observations:observations.length}));

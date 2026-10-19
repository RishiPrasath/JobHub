import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';

const here=path.dirname(fileURLToPath(import.meta.url));
const repo=path.resolve(here,'../../..');
const data=JSON.parse(fs.readFileSync(path.join(here,'slides.json'),'utf8'));
const html=fs.readFileSync(path.join(here,'index.html'),'utf8');
assert(Array.isArray(data.slides)&&data.slides.length>0,'Expected a non-empty slide array');
const slideCount=data.slides.length,mainSlides=data.mainSlides;
assert(Number.isInteger(mainSlides)&&mainSlides>0&&mainSlides<=slideCount,'Invalid main-story boundary');
const tableCount=data.slides.filter(s=>s.layout==='table').length;
const transcriptTableCount=data.slides.filter(s=>Array.isArray(s.rows)).length;
assert.equal(transcriptTableCount,tableCount,'Table content and native table layouts differ');
assert.equal([...html.matchAll(/<article class="slide"/g)].length,slideCount);
assert.equal([...html.matchAll(/<section class="transcript"/g)].length,slideCount);
assert.equal([...html.matchAll(/<details class="notes"/g)].length,slideCount);
assert.equal([...html.matchAll(/<table>/g)].length,tableCount);
assert(html.includes(`Slides 1–${mainSlides}: main briefing.`),'Stale main-story boundary in HTML');
assert.equal([...html.matchAll(/<option value="\d+"/g)].length,slideCount,'Slide selector count differs');
const pngs=[...html.matchAll(/src="data:image\/png;base64,([^"]+)"/g)];
assert.equal(pngs.length,slideCount);
for(const [,b64] of pngs){const b=Buffer.from(b64,'base64');assert.equal(b.readUInt32BE(16),1280);assert.equal(b.readUInt32BE(20),720);}
assert(!/<(?:script|link|iframe)[^>]+(?:src|href)=/i.test(html),'External runtime dependency');
assert(!/\b(?:fetch|XMLHttpRequest|WebSocket)\s*\(/.test(html),'Unexpected network call');
let localLinks=0;
for(const [,href] of html.matchAll(/href="([^"]+)"/g)){
  if(/^https?:/.test(href)){new URL(href.replaceAll('&amp;','&'));continue;}
  assert(fs.existsSync(path.resolve(here,href)),'Missing evidence link '+href);localLinks++;
}
for(const s of data.slides){assert(s.notes&&s.purpose&&s.transition&&s.footnote);for(const ref of s.refs)assert(data.sources[ref]);}
const element=()=>({hidden:false,disabled:false,textContent:'',value:'',attributes:{},events:{},details:{open:false},addEventListener(k,f){this.events[k]=f;},setAttribute(k,v){this.attributes[k]=v;},querySelector(){return this.details;},click(){this.events.click();}});
function navigation(hash=''){
  const slides=Array.from({length:slideCount},element),controls=Object.fromEntries(['prev','next','status','jump','reading','all','print'].map(k=>[k,element()]));
  const events={},classes=new Set();let prints=0;
  const document={querySelectorAll:()=>slides,getElementById:k=>controls[k],body:{classList:{contains:k=>classes.has(k),toggle(k){if(classes.has(k)){classes.delete(k);return false;}classes.add(k);return true;}}},addEventListener(k,f){events[k]=f;}};
  vm.runInNewContext(html.match(/<script>([\s\S]*?)<\/script>/)[1],{document,location:{hash},history:{replaceState(){}},window:{scrollTo(){},print(){prints++;}}},{timeout:1000});
  return {slides,controls,events,classes,prints:()=>prints,key:k=>events.keydown({key:k,preventDefault(){},target:{closest:()=>false}})};
}
const status=number=>`Slide ${number} of ${slideCount}`;
const n=navigation();assert.equal(n.controls.status.textContent,status(1));assert(n.controls.prev.disabled);
n.controls.next.click();assert.equal(n.controls.status.textContent,status(Math.min(2,slideCount)));
n.controls.prev.click();assert.equal(n.controls.status.textContent,status(1));
n.key('ArrowLeft');assert.equal(n.controls.status.textContent,status(1));
n.key('End');assert.equal(n.controls.status.textContent,status(slideCount));assert(n.controls.next.disabled);
n.key('ArrowRight');assert.equal(n.controls.status.textContent,status(slideCount));
n.key('Home');n.key('n');assert(n.slides[0].details.open);
n.key('r');assert(n.classes.has('reading'));assert.equal(n.controls.reading.attributes['aria-pressed'],'true');
n.key('r');assert(!n.classes.has('reading'));
n.controls.all.click();assert(n.classes.has('all'));n.controls.all.click();assert(!n.classes.has('all'));
n.controls.jump.value=String(mainSlides-1);n.controls.jump.events.change();assert.equal(n.controls.status.textContent,status(mainSlides));
if(mainSlides<slideCount){n.controls.next.click();assert.equal(n.controls.status.textContent,status(mainSlides+1));}
n.controls.print.click();assert.equal(n.prints(),1);assert.equal(n.slides.filter(s=>!s.hidden).length,1);
assert.equal(navigation('#'+mainSlides).controls.status.textContent,status(mainSlides));
assert.equal(navigation('#'+(slideCount+1)).controls.status.textContent,status(slideCount));
assert.equal(navigation('#0').controls.status.textContent,status(1));

const reports=['audit-baseline.md','audit-public-and-internal.md','audit-story-and-audience.md'];
const aliases={'R1/W/':'02_research/03_research-rounds/01_public-web-user-insights/runs/2026-10-18-web-based-user-insights/','R2/H/':'02_research/03_research-rounds/02_synthetic-workflow-selection/runs/2026-10-18-synthetic-workflow-comparison/','R2/X/':'02_research/03_research-rounds/02_synthetic-workflow-selection/runs/2026-10-18-pain-practices-and-guidance/','R1/':'02_research/03_research-rounds/01_public-web-user-insights/','R2/':'02_research/03_research-rounds/02_synthetic-workflow-selection/','E/':'02_research/05_evidence/'};
// Parse only explicit inspected-file inventories, never incidental path mentions.
// These reports describe 2026-10-18 coverage, not today's entire research tree.
function section(body,start,end){
  assert(body.includes(start),'Missing historical inventory heading: '+start);
  const rest=body.split(start)[1];
  if(end)assert(rest.includes(end),'Missing historical inventory end: '+end);
  return end?rest.split(end)[0]:rest;
}
const bodies=reports.map(file=>{
  let body=fs.readFileSync(path.join(here,file),'utf8');
  for(const [k,v] of Object.entries(aliases))body=body.replaceAll(k,v);
  let files;
  if(file==='audit-baseline.md')files=[...section(body,'## Exact repository files inspected').matchAll(/^(02_research\/[^\r\n]+)$/gm)];
  else if(file==='audit-public-and-internal.md')files=[...section(body,'### 1.1 Exhaustive assigned file inventory','### 1.2 ').matchAll(/^\| (02_research\/[^|]+) \|/gm)];
  else files=[...section(body,'### Repository files read','### External files').matchAll(/^- `(02_research\/[^`]+)`/gm)];
  return {file,files:new Set(files.map(m=>m[1].trim()).filter(p=>!p.startsWith('02_research/07_presentations/')))};
});
const historicalFiles=[...new Set(bodies.flatMap(b=>[...b.files]))].sort();
assert.equal(historicalFiles.length,136,'Historical baseline inventory changed; review the audit records explicitly');
const historicalSet=new Set(historicalFiles);
const sha256=file=>crypto.createHash('sha256').update(fs.readFileSync(path.join(repo,file))).digest('hex');
const baselineInventory=historicalFiles.map(file=>({file,audits:bodies.filter(b=>b.files.has(file)).map(b=>b.file),present:fs.existsSync(path.join(repo,file))}));
function walk(dir){return fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.name==='07_presentations'?[]:e.isDirectory()?walk(path.join(dir,e.name)):[path.join(dir,e.name)]);}
const corpus=walk(path.join(repo,'02_research')).map(p=>path.relative(repo,p).replaceAll('\\','/')).sort();
const round03Root='02_research/03_research-rounds/03_cross-industry-job-search/';
const inventory=corpus.map(file=>({file,historicalAudits:bodies.filter(b=>b.files.has(file)).map(b=>b.file),currentSha256:sha256(file)}));
const outsideBaseline=corpus.filter(file=>!historicalSet.has(file));
let round03Manifest={status:'Pending separate Round03 file manifest; no new audited coverage asserted.'};
const round03Audit=path.join(here,'audit-round3.md');
if(fs.existsSync(round03Audit)){
  const match=fs.readFileSync(round03Audit,'utf8').match(/<!-- round3-file-manifest -->\s*```json\s*([\s\S]*?)```/);
  assert(match,'Missing Round03 manifest block');
  const manifest=JSON.parse(match[1]);
  assert.equal(manifest.round,'03');assert.equal(manifest.schemaVersion,1);
  assert(Array.isArray(manifest.files)&&manifest.files.length>0);
  assert.equal(new Set(manifest.files.map(e=>e.file)).size,manifest.files.length,'Duplicate manifest file');
  for(const entry of manifest.files){
    assert(entry.file.startsWith(round03Root)&&!entry.file.split('/').includes('..'),'Manifest path outside Round03');
    assert(['full-text-local','selected-records-local'].includes(entry.inspection),'Unspecified inspection depth');
    assert(/^[a-f0-9]{64}$/.test(entry.sha256),'Invalid snapshot hash');
  }
  const changed=manifest.files.filter(e=>!fs.existsSync(path.join(repo,e.file))||sha256(e.file)!==e.sha256).map(e=>e.file);
  round03Manifest={status:changed.length?'Snapshot drift: inspect changed files before refreshing coverage':'Recorded local inspection snapshot matches',inspectedFiles:manifest.files.length,changedSinceSnapshot:changed,scope:manifest.scope};
  const recordFiles=new Map();
  for(const s of data.slides.filter(s=>s.round==='R03')){
    assert(s.claims?.length&&s.urls?.length,'Missing Round03 claim/source mapping');
    for(const c of s.claims){
      assert(c.text&&c.sources.length&&['source-reported','interpretation','hypothesis'].includes(c.kind));
      for(const id of c.sources){
        const r=data.evidenceRecords[id];assert(r,'Missing claim record '+id);
        const entry=manifest.files.find(e=>e.file===r.recordFile);
        assert(entry&&(entry.inspection==='full-text-local'||entry.recordIds?.includes(id)),'Record not inspected in manifest: '+id);
        assert(s.refs.some(key=>data.sources[key][1]===r.recordFile),'Missing slide-local record reference '+id);
        assert(s.urls.some(([,url])=>url===r.url),'Missing slide-local original URL '+id);
        if(!recordFiles.has(r.recordFile))recordFiles.set(r.recordFile,JSON.parse(fs.readFileSync(path.join(repo,r.recordFile),'utf8')));
        const original=recordFiles.get(r.recordFile).sources.find(x=>x.id===id);assert(original,'Unresolved original record '+id);
        for(const field of ['url','passage','publicationDate','eventPeriod','family'])assert.equal(r[field],original[field],'Stale claim metadata '+id+': '+field);
      }
    }
  }
}
const profiles=data.slides.filter(s=>s.industryProfile);
if(profiles.length){
  assert.deepEqual(profiles.map(s=>s.industryProfile).sort(),Array.from({length:13},(_,i)=>'S'+String(i+1).padStart(2,'0')));
  for(const s of profiles){const deep=['S02','S03','S05','S07','S08','S10'].includes(s.industryProfile);assert.equal(s.depth,deep?'deep dive':'breadth only');assert(data.slides.indexOf(s)>=mainSlides,'Industry profile must be in appendix');}
}
const researchCoverage={
  historicalBaseline:{auditDate:'2026-10-18',inventoriedFiles:historicalFiles.length,presentPaths:baselineInventory.filter(x=>x.present).length,missingHistoricalPaths:baselineInventory.filter(x=>!x.present).map(x=>x.file),scope:'Recorded file inspection only. Current bytes have not been re-audited by this verifier.'},
  outsideHistoricalInventory:{files:outsideBaseline,status:'Not covered by the historical audit inventories; additions do not invalidate historical coverage.'},
  round03:{filesObserved:corpus.filter(file=>file.startsWith(round03Root)),inspectionManifest:round03Manifest}
};
const out={checkedAt:new Date().toISOString(),slides:slideCount,mainSlides,appendixSlides:slideCount-mainSlides,nativeTableLayouts:tableCount,embeddedPreviews:pngs.length,transcripts:slideCount,localLinks,navigationLogic:'pass',externalRuntimeDependencies:0,researchFilesObserved:corpus.length,researchCoverage,browserRendering:'not tested',assistiveTechnology:'not tested',baselineInventory,inventory};
const revision=process.env.JOBHUB_DECK_REVISION||'v1';
const privateDir=path.join(path.dirname(here),'.build',path.basename(here),revision);
if(!process.argv.includes('--check-only')){
  fs.mkdirSync(privateDir,{recursive:true});fs.writeFileSync(path.join(privateDir,'static-validation.json'),JSON.stringify(out,null,2));
}
const {inventory:_,baselineInventory:__,...summary}=out;console.log(JSON.stringify(summary));

import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import {createRequire} from 'node:module';
import {fileURLToPath, pathToFileURL} from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const repo = path.resolve(here, '../../..');
const scratch = path.join(path.dirname(here), '.build', path.basename(here));
const previewDir = path.join(scratch, 'previews');
const runtime = process.env.JOBHUB_RUNTIME_ROOT || path.join(os.homedir(), '.cache/codex-runtimes/codex-primary-runtime/dependencies');
process.env.RUNTIME_NODE_MODULES ||= path.join(runtime, 'node/node_modules');
const skill = process.env.JOBHUB_PRESENTATION_SKILL || path.join(os.homedir(), '.codex/plugins/cache/openai-primary-runtime/presentations/26.1017.11052/skills/presentations');
const requireRuntime = createRequire(path.join(runtime, 'node/node_modules/_entry.cjs'));
const {Presentation, PresentationFile} = await import(pathToFileURL(requireRuntime.resolve('@oai/artifact-tool')).href);
const {finalizePresentation, resolvePresentationFont} = await import(pathToFileURL(path.join(skill, 'container_tools/artifact_tool_utils.mjs')).href);
const data = JSON.parse(await fs.readFile(path.join(here, 'slides.json'), 'utf8'));
const run = '02_research/03_research-rounds/02_synthetic-workflow-selection/runs/2026-10-18-pain-practices-and-guidance/';
const refMap = {
  baseline: ['Round 00 research synthesis', '02_research/04_results/00_cross-research-synthesis.md'],
  round1: ['Round 01 public insights', '02_research/03_research-rounds/01_public-web-user-insights/round-synthesis.md'],
  round2: ['Round 02 synthesis', '02_research/03_research-rounds/02_synthetic-workflow-selection/round-synthesis.md'],
  findings: ['Round 02 findings', run+'findings.md'],
  practices: ['Job-seeker practices and original sources', run+'practices-research.md'],
  domain: ['Job fit, pay and domain sources', run+'domain-research.md'],
  coordinator: ['Primary AI-writing study supplement', run+'coordinator-research.md'],
  videos: ['Video insights and timestamped observations', run+'video-research.md'],
  discovery: ['Video discovery and caption provenance', run+'youtube-discovery-log.md'],
  internal: ['Sanitised internal process review', run+'internal-process-review.md'],
  sources: ['Source index', run+'sources.md'],
  coverage: ['Objective coverage', run+'coverage.md'],
  limitations: ['Research limitations', run+'limitations.md'],
  review: ['Independent evidence and quality review', run+'review.md'],
  gate: ['Proposed next step', '02_research/03_research-rounds/02_synthetic-workflow-selection/decision-gate.md'],
  development: ['Earlier development-method findings', '02_research/04_results/development-and-technology/2026-10-18-development-approach.md'],
  competition: ['Earlier competition and positioning findings', '02_research/04_results/market-and-competition/2026-10-18-positioning.md']
};
const externalMap = {
  practices: [
    ['Western Sydney AI-use study', 'https://www.socialventures.org.au/wp-content/uploads/2026/01/Voices-on-Work_-AI-in-Job-Application-.pdf'],
    ['NUS resume guidance', 'https://www.nus.edu.sg/cfg/students/career-resources/create-an-impressive-resume'],
    ['NUS interview guidance', 'https://www.nus.edu.sg/cfg/students/career-resources/ace-your-job-interview']
  ],
  domain: [
    ['MOM occupational wage methodology', 'https://stats.mom.gov.sg/iMAS_Tables1/Wages/Wages_2025/Coverage-and-Methodology-of-OWS-2025.pdf'],
    ['MOM key employment terms', 'https://www.mom.gov.sg/employment-practices/contract-of-service/key-employment-terms'],
    ['NUS offer evaluation', 'https://nus.edu.sg/cfg/students/career-resources/evaluate-job-offers']
  ],
  coordinator: [
    ['Resume-writing experiment', 'https://arxiv.org/abs/2301.08083'],
    ['Employer-post experiment, September 2026 revision', 'https://www.emmawiles.com/storage/jobot.pdf']
  ]
};
for(const s of data.slides) for(const key of s.refs){
  if(!refMap[key]) throw new Error('Unknown reference '+key);
  await fs.access(path.join(repo,refMap[key][1]));
}
await fs.mkdir(previewDir,{recursive:true});
const font = resolvePresentationFont({fontFamily:'Arial'});
const colors = {ink:'#153C3A', text:'#263B3A', muted:'#526967', paper:'#F5F4EF', white:'#FFFFFF', accent:'#A84835'};
const deck = Presentation.create({slideSize:{width:1280,height:720}});
function text(slide,name,value,x,y,w,h,size=27,bold=false,color=colors.text){
  const sh = slide.shapes.add({name,geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0,style:'solid'}});
  sh.text=value;
  sh.text.style={typeface:font,fontSize:size,bold,color,insets:0,verticalAlignment:'top',alignment:'left',wrap:'square',autoFit:'none'};
  return sh;
}
function sourceNotes(s){
  const local = s.refs.map(k=>`${refMap[k][0]}: ${refMap[k][1]}`).join('\n');
  const external = [...new Map(s.refs.flatMap(k=>externalMap[k]||[]).map(a=>[a[1],a])).values()].map(a=>a[0]+': '+a[1]).join('\n');
  return s.notes+'\n\nREPOSITORY SOURCES\n'+local+(external?'\n\nSELECTED ORIGINAL SOURCES\n'+external:'')+'\n\nResearch cutoff: '+data.date+'. Original source dates and limits remain in the ledgers.';
}
for(const [i,s] of data.slides.entries()){
  const slide=deck.slides.add();
  slide.background.fill=i===0?colors.ink:colors.paper;
  if(s.kind==='cover'){
    text(slide,'deck-subject',s.subtitle,72,66,1000,45,25,true,'#D6E6DF');
    text(slide,'cover-title',s.title,72,180,1110,218,78,true,colors.white);
    text(slide,'cover-subtitle',s.lead,76,464,1100,65,31,false,'#D6E6DF');
    text(slide,'cover-date',s.footnote.replace(' · ',' / '),76,635,1080,34,20,false,'#D6E6DF');
  }else{
    text(slide,'slide-title',s.title,72,49,1136,69,44,true,colors.ink);
    text(slide,'slide-lead',s.lead,74,132,1130,76,27,false,colors.muted);
    if(s.kind==='statements'){
      s.items.forEach((item,j)=>{
        const y=232+j*91;
        text(slide,'statement-heading-'+j,item.heading,74,y,1130,36,27,true,colors.ink);
        text(slide,'statement-body-'+j,item.text,74,y+39,1130,48,24,false,colors.text);
      });
    }else if(s.kind==='columns'){
      s.columns.forEach((col,j)=>{
        const x=74+j*588;
        text(slide,'column-heading-'+j,col.heading,x,234,545,42,30,true,colors.ink);
        col.items.forEach((str,k)=>text(slide,`column-${j}-item-${k}`,str,x,302+k*73,535,66,27,false,colors.text));
      });
    }else if(s.kind==='table'){
      const rows=[s.headers,...s.rows];
      const height=s.rows.length===3?330:370;
      const table=slide.tables.add({rows:rows.length,columns:s.headers.length,left:72,top:228,width:1136,height,columnWidths:s.widths,values:rows});
      table.borders.assign({style:'solid',fill:'#D2DDDA',width:0.7});
      table.styleOptions={headerRow:true,bandedRows:false};
      for(let r=0;r<rows.length;r++){
        table.rows[r].height=r===0?49:(height-49)/(rows.length-1);
        for(let c=0;c<rows[r].length;c++){
          const cell=table.getCell(r,c);
          cell.fill=r===0?colors.ink:colors.paper;
          cell.text.style={typeface:font,fontSize:r===0?23:24,bold:r===0,color:r===0?colors.white:colors.text,verticalAlignment:'middle',insets:{left:14,right:14,top:9,bottom:9},wrap:'square',autoFit:'none'};
        }
      }
    }
    text(slide,'evidence-note',s.footnote,74,640,1060,45,18,false,colors.muted);
    text(slide,'page-number',String(i+1).padStart(2,'0'),1152,640,60,35,21,true,colors.accent);
  }
  slide.speakerNotes.text=sourceNotes(s);
  const png=await deck.export({slide,format:'png',scale:1});
  await fs.writeFile(path.join(previewDir,`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await png.arrayBuffer()));
  console.log('Rendered slide '+(i+1));
}
const candidate=path.join(scratch,'candidate.pptx');
await (await PresentationFile.exportPptx(deck)).save(candidate);
const revision=process.env.JOBHUB_DECK_REVISION || 'v2';
const final=path.join(here,`jobhub-research-findings-${revision}.pptx`);
if(await fs.stat(final).then(()=>true).catch(()=>false)) throw new Error('Final PPTX exists. Select a new version filename before rebuilding.');
const result=await finalizePresentation({
  workspaceDir:path.dirname(here),candidatePath:candidate,finalPath:final,
  pythonExecutable:path.join(runtime,'python/python.exe'),
  integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
  layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
  layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit',...data.slides.flatMap((s,i)=>s.kind==='table'?['--require-native-table-slide',String(i+1)]:[])],
  explicitTotalSlideCount:data.slides.length,
  requiredNativeTableOwnerSlides:data.slides.map((s,i)=>s.kind==='table'?i+1:null).filter(Boolean),
  requiredNativeChartOwnerSlides:[],fontPolicy:{basis:'design',families:[font]},verifyArtifactToolImport:true,
  receiptPath:path.join(scratch,`validation-${revision}.json`)
});
console.log('PPTX finalization: '+JSON.stringify(result));

const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const refHtml=s=>s.refs.map(k=>{const [name,p]=refMap[k];return `<li><a href="${esc(path.relative(here,path.join(repo,p)).replaceAll('\\','/'))}">${esc(name)}</a></li>`;}).join('');
function contentHtml(s){
  if(s.kind==='cover')return `<p class="subject">${esc(s.subtitle)}</p><h1>${esc(s.title).replaceAll('\n','<br>')}</h1><p class="cover-lead">${esc(s.lead)}</p>`;
  let body='';
  if(s.kind==='statements')body=`<div class="statements">${s.items.map(a=>`<div><h3>${esc(a.heading)}</h3><p>${esc(a.text)}</p></div>`).join('')}</div>`;
  if(s.kind==='columns')body=`<div class="columns">${s.columns.map(c=>`<section><h3>${esc(c.heading)}</h3><ul>${c.items.map(t=>`<li>${esc(t)}</li>`).join('')}</ul></section>`).join('')}</div>`;
  if(s.kind==='table')body=`<table><colgroup>${s.widths.map(w=>`<col style="width:${w/1136*100}%">`).join('')}</colgroup><thead><tr>${s.headers.map(h=>`<th scope="col">${esc(h)}</th>`).join('')}</tr></thead><tbody>${s.rows.map(r=>`<tr>${r.map(v=>`<td>${esc(v)}</td>`).join('')}</tr>`).join('')}</tbody></table>`;
  return `<h2>${esc(s.title)}</h2><p class="lead">${esc(s.lead)}</p>${body}`;
}
const sections=data.slides.map((s,i)=>`<article class="slide ${s.kind==='cover'?'cover':''}" id="slide-${i+1}" aria-label="Slide ${i+1} of ${data.slides.length}" ${i?'hidden':''}><div class="canvas">${contentHtml(s)}<footer><span>${esc(s.footnote.replace(' · ',' / '))}</span><span>${i+1} / ${data.slides.length}</span></footer></div><details class="notes"><summary>Reading notes and sources</summary><p>${esc(s.notes)}</p><ul>${refHtml(s)}</ul>${s.refs.some(k=>externalMap[k])?`<p>Selected original sources</p><ul>${[...new Map(s.refs.flatMap(k=>externalMap[k]||[]).map(a=>[a[1],a])).values()].map(a=>`<li><a href="${esc(a[1])}" target="_blank" rel="noopener noreferrer">${esc(a[0])}</a></li>`).join('')}</ul>`:''}</details></article>`).join('\n');
const html=`<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="JobHub research findings, Rounds 00–02. Offline reading deck with sources."><title>${esc(data.title)}</title><style>
:root{color-scheme:light;font-family:Arial,Helvetica,sans-serif;color:#263b3a;background:#e7ece8}*{box-sizing:border-box}body{margin:0}button{font:inherit;cursor:pointer;border:1px solid #aabcb6;background:white;color:#153c3a;border-radius:4px;padding:10px 15px}button:disabled{opacity:.45;cursor:default}button:focus-visible,a:focus-visible,summary:focus-visible{outline:3px solid #a84835;outline-offset:3px}nav{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:14px 24px;flex-wrap:wrap;background:#fff;position:sticky;top:0;z-index:10}nav .buttons{display:flex;gap:8px}#status{font-size:16px}main{padding:24px}.slide{max-width:1280px;margin:0 auto 28px}.canvas{container-type:inline-size;background:#f5f4ef;aspect-ratio:16/9;padding:3.8% 5.625% 3%;position:relative;overflow:hidden;box-shadow:0 5px 24px #153c3a15}h1,h2,h3,p{margin:0}h2{font-size:clamp(24px,3.45cqw,44px);line-height:1.16;color:#153c3a;margin-bottom:1.1cqw}p.lead{font-size:2.1cqw;line-height:1.35;color:#526967;min-height:7.1cqw}.statements{display:flex;flex-direction:column;gap:1.6cqw}.statements h3{font-size:2.1cqw;line-height:1.2;color:#153c3a}.statements p{font-size:1.87cqw;line-height:1.35;margin-top:.55cqw}.columns{display:grid;grid-template-columns:1fr 1fr;gap:4.4cqw}.columns h3{font-size:2.34cqw;color:#153c3a;margin-bottom:1.5cqw}.columns ul{padding:0;margin:0;list-style:none}.columns li{font-size:2.1cqw;line-height:1.3;margin-bottom:1.6cqw}table{border-collapse:collapse;table-layout:fixed;width:100%;font-size:1.87cqw;line-height:1.25}th,td{padding:1.2cqw 1.1cqw;border:1px solid #d2ddda;text-align:left;vertical-align:middle}th{background:#153c3a;color:white;font-size:1.8cqw}footer{position:absolute;bottom:3.1cqw;left:5.8%;right:5.8%;display:flex;gap:2cqw;justify-content:space-between;font-size:1.4cqw;line-height:1.3;color:#526967}footer>span:first-child{max-width:94%}footer>span:last-child{white-space:nowrap;color:#a84835;font-weight:700}.cover .canvas{background:#153c3a;color:#fff}.cover .subject{font-size:2cqw;color:#d6e6df;margin-top:.7cqw;font-weight:700}.cover h1{font-size:6.1cqw;line-height:1.12;margin-top:5.5cqw}.cover-lead{font-size:2.4cqw;color:#d6e6df;margin-top:4.5cqw}.cover footer,.cover footer>span:last-child{color:#d6e6df}.notes{font-size:18px;line-height:1.6;background:white;padding:18px 24px}.notes p{margin:12px 0}.notes summary{cursor:pointer;color:#153c3a;font-weight:700}.notes a{color:#155c85}.reading .slide[hidden]{display:block}.reading .notes{display:block}#help{text-align:center;color:#526967;font-size:14px;margin:20px}
@media(max-width:700px){nav{padding:10px}main{padding:10px}.canvas{aspect-ratio:auto;min-height:80vh;padding:30px 24px 86px;overflow:visible}h2{font-size:29px}.lead{font-size:19px!important;margin:18px 0 26px!important;min-height:0!important}.statements{gap:22px}.statements h3,.columns h3{font-size:21px}.statements p,.columns li{font-size:18px}.columns{grid-template-columns:1fr;gap:28px}.columns li{margin-bottom:14px}.columns h3{margin-bottom:16px}table{font-size:15px}th{font-size:15px}th,td{padding:10px 8px;overflow-wrap:anywhere}footer{font-size:12px;bottom:24px;left:24px;right:24px}.cover h1{font-size:50px;margin-top:75px}.cover .subject{font-size:20px}.cover-lead{font-size:23px;margin-top:45px}.notes{font-size:16px}.canvas h2{line-height:1.15}}
@media print{@page{size:13.333in 7.5in;margin:0}body{background:white}nav,#help,.notes{display:none!important}main{padding:0}.slide,.slide[hidden]{display:block!important;margin:0;max-width:none;break-after:page}.canvas{box-shadow:none;width:100vw;height:56.25vw;aspect-ratio:16/9;print-color-adjust:exact;-webkit-print-color-adjust:exact}a{color:inherit}}
</style></head><body><nav aria-label="Presentation controls"><div class="buttons"><button id="prev" aria-label="Previous slide">Previous</button><button id="next" aria-label="Next slide">Next</button></div><span id="status" aria-live="polite"></span><div class="buttons"><button id="read" aria-pressed="false">Read all slides</button><button id="print">Print / Save PDF</button></div></nav><main>${sections}</main><p id="help">Left / Right: change slide. Home / End: first or last. N: reading notes. Works offline.</p><script>
const slides=[...document.querySelectorAll('article.slide')];let current=Math.max(0,Math.min(slides.length-1,(parseInt(location.hash.slice(1),10)||1)-1));let reading=false;const previous=document.getElementById('prev'),next=document.getElementById('next'),status=document.getElementById('status'),read=document.getElementById('read');
function show(n){current=Math.max(0,Math.min(slides.length-1,n));slides.forEach((s,i)=>s.hidden=i!==current);status.textContent='Slide '+(current+1)+' of '+slides.length;previous.disabled=current===0;next.disabled=current===slides.length-1;history.replaceState(null,'','#'+(current+1));if(!reading)window.scrollTo(0,0)}
previous.addEventListener('click',()=>show(current-1));next.addEventListener('click',()=>show(current+1));read.addEventListener('click',()=>{reading=!reading;document.body.classList.toggle('reading',reading);read.setAttribute('aria-pressed',String(reading));read.textContent=reading?'Slide view':'Read all slides'});document.getElementById('print').addEventListener('click',()=>window.print());document.addEventListener('keydown',e=>{if(e.target.closest('a,summary,input,textarea'))return;if(e.key==='ArrowRight'||e.key==='PageDown'){e.preventDefault();show(current+1)}if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();show(current-1)}if(e.key==='Home'){e.preventDefault();show(0)}if(e.key==='End'){e.preventDefault();show(slides.length-1)}if(e.key.toLowerCase()==='n'){const d=slides[current].querySelector('details');d.open=!d.open}});show(current);
</script></body></html>`;
await fs.writeFile(path.join(here,'index.html'),html);
const markdown=['---','marp: true','paginate: true','title: JobHub Research Findings','---','',...data.slides.flatMap((s,i)=>[
  (i?'---\n\n':'')+'# '+s.title.replaceAll('\n',' '),'',s.lead,'',
  ...(s.items?s.items.flatMap(a=>['## '+a.heading,'',a.text,'']):[]),
  ...(s.columns?s.columns.flatMap(c=>['## '+c.heading,'',...c.items.map(t=>'- '+t),'']):[]),
  ...(s.rows?['| '+s.headers.join(' | ')+' |','| '+s.headers.map(()=>'---').join(' | ')+' |',...s.rows.map(r=>'| '+r.join(' | ')+' |'),'']:[]),
  s.footnote,'','<!--\n'+sourceNotes(s)+'\n-->',''
])].join('\n');
await fs.writeFile(path.join(here,'slides.md'),markdown);
console.log(JSON.stringify({slides:data.slides.length,html:path.join(here,'index.html'),pptx:final,previews:previewDir}));

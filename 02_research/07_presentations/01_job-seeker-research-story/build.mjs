import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import {createRequire} from 'node:module';
import {fileURLToPath,pathToFileURL} from 'node:url';

const here=path.dirname(fileURLToPath(import.meta.url));
const repo=path.resolve(here,'../../..');
const runtime=process.env.JOBHUB_RUNTIME_ROOT||path.join(os.homedir(),'.cache/codex-runtimes/codex-primary-runtime/dependencies');
const skill=process.env.JOBHUB_PRESENTATION_SKILL||path.join(os.homedir(),'.codex/plugins/cache/openai-primary-runtime/presentations/26.1017.11052/skills/presentations');
process.env.RUNTIME_NODE_MODULES||=path.join(runtime,'node/node_modules');
const req=createRequire(path.join(runtime,'node/node_modules/_entry.cjs'));
const {Presentation,PresentationFile}=await import(pathToFileURL(req.resolve('@oai/artifact-tool')).href);
const {finalizePresentation,resolvePresentationFont}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
const data=JSON.parse(await fs.readFile(path.join(here,'slides.json'),'utf8'));
const revision=process.env.JOBHUB_DECK_REVISION||'v1';
const scratch=path.join(path.dirname(here),'.build',path.basename(here),revision);
const previews=path.join(scratch,'previews');
const final=path.join(here,`jobhub-domain-brief-${revision}.pptx`);
if(await fs.stat(final).then(()=>true).catch(()=>false))throw new Error('Validated export exists; choose a fresh JOBHUB_DECK_REVISION.');
await fs.mkdir(previews,{recursive:true});
for(const [key,[,ref]] of Object.entries(data.sources)){
  await fs.access(path.join(repo,ref)).catch(()=>{throw new Error('Missing source '+key+': '+ref);});
}
for(const s of data.slides)for(const ref of s.refs)if(!data.sources[ref])throw new Error('Unknown source '+ref);
const font=resolvePresentationFont({fontFamily:'Arial'});
const C={navy:'#102235',paper:'#FAF6EE',ink:'#172D40',muted:'#52616B',orange:'#B94B28',gold:'#F1C58A',teal:'#166B65',pale:'#D7E1E3',white:'#FFFFFF'};
const deck=Presentation.create({slideSize:{width:1280,height:720}});
const txt=(sl,name,value,x,y,w,h,size=27,bold=false,color=C.ink)=>{
  const sh=sl.shapes.add({name,geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0,style:'solid'}});
  sh.text=String(value);sh.text.style={typeface:font,fontSize:size,bold,color,insets:0,verticalAlignment:'top',alignment:'left',wrap:'square',autoFit:'none'};
  return sh;
};
const line=(sl,name,x,y,w,color=C.pale)=>sl.shapes.add({name,geometry:'line',position:{left:x,top:y,width:w,height:0},fill:'none',line:{fill:color,width:2,style:'solid'}});
async function picture(sl,filename,alt){
  const bytes=await fs.readFile(path.join(here,filename));
  sl.images.add({name:'editorial illustration',blob:bytes.buffer.slice(bytes.byteOffset,bytes.byteOffset+bytes.byteLength),contentType:'image/png',alt,fit:'cover',position:{left:0,top:0,width:1280,height:720}});
}
const references=s=>s.refs.map(k=>`${data.sources[k][0]}: ${data.sources[k][1]}`).join('\n');
function claimNotes(s){return (s.claims||[]).map(c=>`${c.kind}: ${c.text}\n${c.sources.map(id=>{
  const r=data.evidenceRecords[id];
  if(!r)throw new Error('Missing claim record '+id);
  return `${id}: ${r.recordFile}\nOriginal: ${r.url}\nLocator: ${r.passage}\nPublished: ${r.publicationDate}. Underlying period: ${r.eventPeriod}.\nBoundary: ${r.limits}`;
}).join('\n')}`).join('\n\n');}
function notes(s){return `${s.notes}\n\n${s.claims?.length?'CLAIM-LEVEL EVIDENCE\n'+claimNotes(s)+'\n\n':''}REPOSITORY EVIDENCE\n${references(s)}\n\nSELECTED ORIGINAL SOURCES\n${(s.urls||[]).map(([n,u])=>n+': '+u).join('\n')||'Original source URLs and locators are in the linked repository evidence.'}\n\nUnqualified P/D/C/I/V IDs belong to expanded Round 02. R3- IDs belong to the 19 October Round 03 run. Earlier findings retain their original periods. Briefing cutoff: ${data.date}. Historical proposals are not product decisions.`;}
const tableOwners=[];
const previewFiles=[];
for(const [index,s] of data.slides.entries()){
  const sl=deck.slides.add();
  const dark=Boolean(s.dark||['cover','opening','image','duostat','closing'].includes(s.layout));
  sl.background.fill=dark?C.navy:C.paper;
  const ink=dark?C.white:C.ink,muted=dark?C.pale:C.muted,accent=dark?C.gold:C.orange;
  if(s.image)await picture(sl,s.image,'Fictional AI-generated editorial illustration, not a research participant or evidence.');
  if(s.layout==='cover'){
    txt(sl,'title',s.title,76,172,650,230,76,true,C.white);
    txt(sl,'subtitle',s.lead,80,476,550,85,31,false,C.pale);
  }else if(s.layout==='image'){
    txt(sl,'title',s.title,76,126,485,286,54,true,C.white);
    txt(sl,'subtitle',s.lead,80,454,490,120,29,false,C.pale);
  }else if(s.layout==='opening'){
    txt(sl,'title',s.title,76,190,640,240,80,true,C.white);
    txt(sl,'subtitle',s.lead,80,490,550,95,30,false,C.pale);
    s.items.forEach((it,j)=>{txt(sl,'question-'+j,it.heading,760,224+j*120,440,46,33,true,C.gold);txt(sl,'question-detail-'+j,it.text,760,274+j*120,430,70,26,false,C.pale);});
  }else if(s.layout==='closing'){
    txt(sl,'title',s.title,76,60,1136,110,48,true,C.white);
    txt(sl,'synthesis',s.lead,76,218,1110,250,62,true,C.white);
    s.items.forEach((it,j)=>{txt(sl,'discussion-'+j,it.heading,76+j*590,514,540,37,26,true,C.gold);txt(sl,'discussion-detail-'+j,it.text,76+j*590,560,530,70,24,false,C.pale);});
  }else{
    txt(sl,'title',s.title,76,54,1130,114,46,true,ink);
    txt(sl,'lead',s.lead,80,171,1115,72,27,false,muted);
    if(s.layout==='journey'){
      line(sl,'journey-sequence',102,335,1064,C.teal);
      s.steps.forEach((st,j)=>{const x=80+j*191;txt(sl,'stage-number-'+j,String(j+1).padStart(2,'0'),x,259,160,68,56,true,C.orange);txt(sl,'stage-'+j,st.heading,x,366,165,45,27,true,C.ink);txt(sl,'stage-question-'+j,st.text,x,425,165,100,25,false,C.muted);});
    }else if(['columns','contrast'].includes(s.layout)){
      s.columns.forEach((col,j)=>{
        const x=80+j*590,n=col.items.length,step=n===2?128:87;
        txt(sl,'column-heading-'+j,col.heading,x,266,535,52,31,true,s.layout==='contrast'&&j===1?C.orange:C.teal);
        col.items.forEach((it,k)=>txt(sl,`column-${j}-detail-${k}`,it,x,334+k*step,525,n===2?112:78,27,false,C.ink));
      });
    }else if(s.layout==='case'){
      txt(sl,'case-main',s.headline,80,286,535,225,49,true,C.orange);
      s.items.forEach((it,j)=>{txt(sl,'case-label-'+j,it.heading,680,270+j*165,520,46,30,true,C.teal);txt(sl,'case-text-'+j,it.text,680,325+j*165,510,112,26,false,C.ink);});
    }else if(s.layout==='table'){
      tableOwners.push(index+1);
      const rows=[s.headers,...s.rows],height=s.tableHeight??(s.rows.length===3?330:338);
      const tb=sl.tables.add({rows:rows.length,columns:s.headers.length,left:76,top:s.tableTop??266,width:1136,height,columnWidths:s.widths,values:rows});
      tb.borders.assign({style:'solid',fill:'#D9D8D2',width:0.7});
      tb.styleOptions={headerRow:true,bandedRows:false};
      const headerHeight=s.tableHeaderHeight??48;
      rows.forEach((r,ri)=>{tb.rows[ri].height=ri===0?headerHeight:(height-headerHeight)/(rows.length-1);r.forEach((_,ci)=>{const cell=tb.getCell(ri,ci);cell.fill=ri===0?C.navy:C.paper;cell.text.style={typeface:font,fontSize:s.tableFontSize??(ri===0?24:25),bold:ri===0,color:ri===0?C.white:C.ink,verticalAlignment:'middle',insets:{left:14,right:14,top:s.tableInset??8,bottom:s.tableInset??8},wrap:'square',autoFit:'none'};});});
    }else if(s.layout==='flow'){
      const n=s.steps.length,gap=34,w=(1136-gap*(n-1))/n;
      s.steps.forEach((st,j)=>{const x=80+j*(w+gap);if(s.ordered!==false)txt(sl,'diagram-index-'+j,String(j+1).padStart(2,'0'),x,270,w,65,50,true,accent);txt(sl,'diagram-heading-'+j,st.heading,x,s.ordered===false?296:362,w,75,s.ordered===false?35:31,true,s.ordered===false?(dark?C.gold:C.teal):ink);txt(sl,'diagram-detail-'+j,st.text,x,s.ordered===false?405:446,w-8,125,27,false,muted);if(j<n-1&&s.ordered!==false)line(sl,'diagram-sequence-'+j,x+80,316,w+gap-80,dark?'#8097A5':C.teal);});
    }else if(s.layout==='stat'){
      txt(sl,'reported-effect',s.stat,76,258,510,190,174,true,C.orange);
      txt(sl,'effect-definition',s.statLabel,86,471,465,105,32,true,C.ink);
      s.items.forEach((it,j)=>{txt(sl,'study-context-'+j,it.heading,680,270+j*175,520,74,30,true,C.teal);txt(sl,'study-context-detail-'+j,it.text,680,353+j*175,510,95,26,false,C.ink);});
    }else if(s.layout==='duostat'){
      s.metrics.forEach((m,j)=>{const x=80+j*590;txt(sl,'reported-effect-'+j,m.value,x,268,530,170,135,true,C.gold);txt(sl,'effect-definition-'+j,m.label,x+5,443,520,70,30,false,C.white);});
    }else throw new Error('Unsupported layout '+s.layout);
    if(s.takeaway)txt(sl,'takeaway',s.takeaway,80,s.layout==='duostat'?545:596,1115,53,s.layout==='duostat'?32:25,true,dark?C.white:C.teal);
  }
  txt(sl,'evidence-boundary',s.footnote,80,656,1060,45,18,false,muted);
  txt(sl,'slide-number',String(index+1).padStart(2,'0'),1162,656,54,34,21,true,accent);
  sl.speakerNotes.text=notes(s);
  const file=path.join(previews,`slide-${String(index+1).padStart(2,'0')}.png`);
  const png=await deck.export({slide:sl,format:'png',scale:1});
  await fs.writeFile(file,new Uint8Array(await png.arrayBuffer()));previewFiles.push(file);
  console.log('Rendered '+(index+1)+'/'+data.slides.length+': '+s.title.replaceAll('\n',' '));
}
const candidate=path.join(scratch,'candidate.pptx');
await (await PresentationFile.exportPptx(deck)).save(candidate);
const receipt=await finalizePresentation({workspaceDir:path.dirname(here),candidatePath:candidate,finalPath:final,pythonExecutable:path.join(runtime,'python/python.exe'),integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit',...tableOwners.flatMap(n=>['--require-native-table-slide',String(n)])],explicitTotalSlideCount:data.slides.length,requiredNativeTableOwnerSlides:tableOwners,requiredNativeChartOwnerSlides:[],fontPolicy:{basis:'design',families:[font]},verifyArtifactToolImport:true,receiptPath:path.join(scratch,'validation.json')});
console.log('Finalised '+final+' with '+tableOwners.length+' editable tables.');

const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
function transcript(s){
  return `<h2>${esc(s.title).replaceAll('\n',' ')}</h2><p class="lead">${esc(s.lead).replaceAll('\n','<br>')}</p>`+
  (s.headline?`<p>${esc(s.headline).replaceAll('\n','<br>')}</p>`:'')+
  (s.stat?`<p><strong>${esc(s.stat)} ${esc(s.statLabel)}</strong></p>`:'')+
  (s.metrics?`<dl>${s.metrics.map(m=>`<dt>${esc(m.value)}</dt><dd>${esc(m.label)}</dd>`).join('')}</dl>`:'')+
  (s.items?s.items.map(it=>`<h3>${esc(it.heading)}</h3><p>${esc(it.text)}</p>`).join(''):'')+
  (s.columns?`<div class="reading-columns">${s.columns.map(c=>`<section><h3>${esc(c.heading)}</h3><ul>${c.items.map(it=>`<li>${esc(it)}</li>`).join('')}</ul></section>`).join('')}</div>`:'')+
  (s.steps?`<${s.ordered===false?'ul':'ol'}>${s.steps.map(st=>`<li><strong>${esc(st.heading)}</strong>: ${esc(st.text)}</li>`).join('')}</${s.ordered===false?'ul':'ol'}>`:'')+
  (s.rows?`<div class="table-scroll"><table><thead><tr>${s.headers.map(h=>`<th scope="col">${esc(h)}</th>`).join('')}</tr></thead><tbody>${s.rows.map(r=>`<tr>${r.map(t=>`<td>${esc(t)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`:'')+
  (s.takeaway?`<p class="takeaway">${esc(s.takeaway)}</p>`:'')+
  `<p class="boundary">${esc(s.footnote)}</p>`;
}
let articles='';
for(const [i,s] of data.slides.entries()){
  const base64=(await fs.readFile(previewFiles[i])).toString('base64');
  const refs=s.refs.map(k=>{const [name,p]=data.sources[k];return `<li><a href="${esc(path.relative(here,path.join(repo,p)).replaceAll('\\','/'))}">${esc(name)}</a></li>`;}).join('');
  const urls=(s.urls||[]).map(([n,u])=>`<li><a href="${esc(u)}" target="_blank" rel="noopener noreferrer">${esc(n)}</a></li>`).join('');
  articles+=`<article class="slide" id="slide-${i+1}" aria-label="Slide ${i+1} of ${data.slides.length}" ${i?'hidden':''}><img class="visual" src="data:image/png;base64,${base64}" alt="${esc(s.title.replaceAll('\n',' '))}. The complete text and explanation follow in reading mode." width="1280" height="720"><section class="transcript" aria-label="Slide text">${transcript(s)}</section><details class="notes"><summary>Explanation and sources</summary><p>${esc(s.notes)}${s.claims?.length?'<br><br>'+esc(claimNotes(s)).replaceAll('\n','<br>'):''}</p><ul>${refs}${urls}</ul></details></article>`;
}
const html=`<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>${esc(data.title)}</title><meta name="description" content="An offline evidence-backed introduction to job hunting, AI assistance and the research behind JobHub."><style>
:root{color-scheme:light;font-family:Arial,Helvetica,sans-serif;background:#102235;color:#172d40}*{box-sizing:border-box}body{margin:0}nav{display:flex;align-items:center;gap:12px;flex-wrap:wrap;padding:12px 20px;background:#faf6ee;position:sticky;top:0;z-index:5}button,select{font:inherit;font-size:16px;padding:10px 12px;border:1px solid #9da8aa;border-radius:3px;color:#172d40;background:white;cursor:pointer}button:disabled{opacity:.45;cursor:default}button:focus-visible,select:focus-visible,a:focus-visible,summary:focus-visible{outline:3px solid #b94b28;outline-offset:3px}#status{margin-right:auto;font-size:16px}select{max-width:270px}main{padding:20px}.slide{max-width:1280px;margin:0 auto 26px;background:#faf6ee}.slide[hidden]{display:none}.visual{display:block;width:100%;height:auto}.transcript{display:none;padding:32px 40px;font-size:20px;line-height:1.6;max-width:1050px;margin:auto}h2{font-size:38px;line-height:1.2;margin:0 0 20px}h3{font-size:25px;line-height:1.3;margin:28px 0 12px}.lead{font-size:23px;color:#52616b}.boundary{font-size:17px;border-top:1px solid #c8ceca;padding-top:18px}.takeaway{font-weight:bold;color:#166b65}.reading-columns{display:grid;grid-template-columns:1fr 1fr;gap:42px}li{margin-bottom:12px}.table-scroll{overflow-x:auto}table{border-collapse:collapse;font-size:18px;width:100%}th,td{border:1px solid #bfc8c8;padding:12px;text-align:left}th{background:#102235;color:white}.notes{padding:18px 32px;font-size:18px;line-height:1.6}.notes p{max-width:100ch}.notes a{color:#155a80}.notes summary{cursor:pointer;font-weight:bold}#help{color:#e4e8e7;text-align:center;font-size:15px;margin:22px}body.reading .visual{display:none}body.reading .transcript{display:block}body.all .slide[hidden]{display:block}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}@media(max-width:700px){nav{padding:10px;gap:8px}main{padding:8px}.transcript{padding:22px;font-size:19px}h2{font-size:30px}.reading-columns{grid-template-columns:1fr;gap:12px}.notes{padding:18px}select{max-width:100%}#status{margin-right:0}.visual{min-height:0}}
@media print{@page{size:13.333in 7.5in;margin:0}nav,#help,.notes,.transcript{display:none!important}main{padding:0}.slide,.slide[hidden]{display:block!important;max-width:none;margin:0;break-after:page}.visual,body.reading .visual{display:block!important;width:100%;height:auto;print-color-adjust:exact;-webkit-print-color-adjust:exact}}
</style></head><body><nav aria-label="Presentation controls"><button id="prev" aria-label="Previous slide">Previous</button><button id="next" aria-label="Next slide">Next</button><span id="status" aria-live="polite"></span><label class="sr-only" for="jump">Jump to slide</label><select id="jump">${data.slides.map((s,i)=>`<option value="${i}">${i+1}. ${esc(s.title.replaceAll('\n',' '))}</option>`).join('')}</select><button id="reading" aria-pressed="false">Readable text</button><button id="all" aria-pressed="false">Show all</button><button id="print">Print / PDF</button></nav><main>${articles}</main><p id="help">Arrows: change slide. Home / End: first or last. N: notes. R: readable text. Slides 1–${data.mainSlides}: main briefing. Remaining slides: appendix.</p><script>
const slides=[...document.querySelectorAll('article.slide')];let current=Math.max(0,Math.min(slides.length-1,(parseInt(location.hash.slice(1),10)||1)-1));const byId=id=>document.getElementById(id);const prev=byId('prev'),next=byId('next'),status=byId('status'),jump=byId('jump');
function show(n){current=Math.max(0,Math.min(slides.length-1,n));slides.forEach((s,i)=>s.hidden=i!==current);prev.disabled=current===0;next.disabled=current===slides.length-1;status.textContent='Slide '+(current+1)+' of '+slides.length;jump.value=String(current);history.replaceState(null,'','#'+(current+1));if(!document.body.classList.contains('all'))window.scrollTo(0,0)}
prev.addEventListener('click',()=>show(current-1));next.addEventListener('click',()=>show(current+1));jump.addEventListener('change',()=>show(Number(jump.value)));
function toggleMode(id,cls,on,off){const state=document.body.classList.toggle(cls);byId(id).setAttribute('aria-pressed',String(state));byId(id).textContent=state?on:off;}
byId('reading').addEventListener('click',()=>toggleMode('reading','reading','Slide visuals','Readable text'));byId('all').addEventListener('click',()=>toggleMode('all','all','One slide','Show all'));byId('print').addEventListener('click',()=>window.print());
document.addEventListener('keydown',e=>{if(e.target.closest('a,summary,input,textarea,select'))return;const k=e.key.toLowerCase();if(['arrowright','pagedown','arrowleft','pageup','home','end'].includes(k)){e.preventDefault();show(k==='home'?0:k==='end'?slides.length-1:current+(['arrowright','pagedown'].includes(k)?1:-1));}if(k==='n'){const d=slides[current].querySelector('details');d.open=!d.open;}if(k==='r')byId('reading').click();});show(current);
</script></body></html>`;
await fs.writeFile(path.join(here,'index.html'),html);
const storyboard=['# Audience and storyboard','',data.audience,'','Research question: What work and decisions does job hunting involve, how do people use assistance, and what does the evidence leave unresolved?','','Main story: slides 1–'+data.mainSlides+'. Appendix: remaining slides.','',...data.slides.flatMap((s,i)=>['## '+(i+1)+'. '+s.title.replaceAll('\n',' '),'','Purpose: '+s.purpose,'','Transition: '+s.transition,'','Evidence: '+s.refs.map(k=>data.sources[k][0]).join('; '),''])].join('\n');
await fs.writeFile(path.join(here,'storyboard.md'),storyboard);
const claimMap=['# Slide-to-evidence map','','Unqualified P/D/C/I/V IDs belong to expanded Round 02. R3- IDs belong to the Round 03 run dated 19 October 2026. Same unqualified IDs in historical runs are different records. This is a communication map, not new empirical evidence.','',...data.slides.flatMap((s,i)=>['## '+(i+1)+'. '+s.title.replaceAll('\n',' '),'',s.footnote,'',s.notes,'',...(s.claims?.length?[claimNotes(s),'']:[]),...s.refs.map(k=>'- ['+data.sources[k][0]+']('+path.relative(here,path.join(repo,data.sources[k][1])).replaceAll('\\','/')+')'),...(s.urls||[]).map(([n,u])=>'- ['+n+']('+u+')'),''])].join('\n');
await fs.writeFile(path.join(here,'claim-map.md'),claimMap);
const md=['---','marp: true','paginate: true','title: '+data.title,'---','',...data.slides.flatMap((s,i)=>[(i?'---\n\n':'')+'# '+s.title.replaceAll('\n',' '),'',s.lead,'',...(s.stat?[s.stat+' '+s.statLabel,'']:[]),...(s.metrics?s.metrics.map(m=>m.value+' '+m.label):[]),...(s.items?s.items.flatMap(it=>['## '+it.heading,'',it.text,'']):[]),...(s.columns?s.columns.flatMap(c=>['## '+c.heading,'',...c.items.map(t=>'- '+t),'']):[]),...(s.steps?s.steps.map((st,j)=>`${j+1}. ${st.heading}: ${st.text}`):[]),...(s.rows?['| '+s.headers.join(' | ')+' |','| '+s.headers.map(()=>'---').join(' | ')+' |',...s.rows.map(r=>'| '+r.join(' | ')+' |')]:[]),'',s.takeaway||'',s.footnote,'','<!--\n'+notes(s)+'\n-->',''])].join('\n');
await fs.writeFile(path.join(here,'slides.md'),md);
await fs.writeFile(path.join(scratch,'build-summary.json'),JSON.stringify({slides:data.slides.length,main:data.mainSlides,tables:tableOwners,previewFiles,pptx:final,sha256:receipt.finalSha256},null,2));
console.log(JSON.stringify({slides:data.slides.length,main:data.mainSlides,pptx:final,html:path.join(here,'index.html'),previews}));

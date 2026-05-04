(function(){
  const DEFAULTS = /*EDITMODE-BEGIN*/{
    "accentHue": 28,
    "accentChroma": 0.22,
    "accentLight": 0.58,
    "displayFont": "Gmarket Sans",
    "bodyFont": "Pretendard",
    "density": 1.0,
    "containerWidth": 1200,
    "lhDisplay": 1.15,
    "lhBody": 1.7,
    "sectionsOn": {
      "hero": true, "statement": true, "pain": true, "solution": true,
      "hook": true, "usp": true, "featSplit": true, "featStrip": true,
      "info": true, "ing": true, "howto": true, "scene": true,
      "ba": true, "compare": true, "reviews": true, "quote": true,
      "timeline": true, "bstory": true, "faq": true, "cta": true
    }
  }/*EDITMODE-END*/;

  const state = JSON.parse(JSON.stringify(DEFAULTS));
  try { const saved = localStorage.getItem('tweaks'); if (saved) Object.assign(state, JSON.parse(saved)); } catch(e) {}

  const root = document.documentElement;
  function apply(){
    root.style.setProperty('--accent', `oklch(${state.accentLight} ${state.accentChroma} ${state.accentHue})`);
    root.style.setProperty('--font-display', `'${state.displayFont}', 'Pretendard', system-ui, sans-serif`);
    root.style.setProperty('--font-body', `'${state.bodyFont}', 'Gmarket Sans', system-ui, sans-serif`);
    root.style.setProperty('--section-pad-y', `${Math.round(120*state.density)}px`);
    root.style.setProperty('--section-pad-y-sm', `${Math.round(72*state.density)}px`);
    root.style.setProperty('--container-wide', `${state.containerWidth}px`);
    root.style.setProperty('--lh-display', state.lhDisplay);
    root.style.setProperty('--lh-body', state.lhBody);
    Object.entries(state.sectionsOn||{}).forEach(([k,v])=>{
      document.querySelectorAll(`[data-sec="${k}"]`).forEach(el=>{ el.style.display = v ? '' : 'none'; });
    });
    try { localStorage.setItem('tweaks', JSON.stringify(state)); } catch(e){}
  }
  apply();

  const PRESETS = {
    ember: {accentLight:0.58, accentChroma:0.22, accentHue:28},
    forest: {accentLight:0.52, accentChroma:0.14, accentHue:145},
    cobalt: {accentLight:0.55, accentChroma:0.18, accentHue:250},
    amber: {accentLight:0.72, accentChroma:0.17, accentHue:70},
    mono: {accentLight:0.20, accentChroma:0.00, accentHue:0}
  };

  let mounted = false, panel = null;
  function build(){
    if (mounted) return;
    panel = document.createElement('div');
    panel.id = 'tweak-panel';
    panel.innerHTML = `
      <style>
        #tweak-panel{position:fixed;right:16px;bottom:16px;width:320px;max-height:80vh;overflow:auto;
          background:#fff;color:#0a0a0a;border:2px solid #0a0a0a;z-index:9999;
          font-family:'Pretendard',system-ui,sans-serif;font-size:13px;box-shadow:8px 8px 0 #0a0a0a;}
        #tweak-panel h3{font-family:'Gmarket Sans',sans-serif;font-size:16px;font-weight:700;
          padding:14px 18px;border-bottom:2px solid #0a0a0a;display:flex;justify-content:space-between;align-items:center;}
        #tweak-panel .tp-close{background:none;border:0;font-size:20px;cursor:pointer;line-height:1}
        #tweak-panel .tp-body{padding:16px 18px;display:flex;flex-direction:column;gap:18px}
        #tweak-panel .tp-group{display:flex;flex-direction:column;gap:8px}
        #tweak-panel label{font-family:'JetBrains Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:0.1em;color:#555;display:flex;justify-content:space-between}
        #tweak-panel input[type=range]{width:100%;accent-color:#0a0a0a}
        #tweak-panel .tp-presets{display:grid;grid-template-columns:repeat(5,1fr);gap:6px}
        #tweak-panel .tp-preset{height:28px;border:2px solid #0a0a0a;cursor:pointer}
        #tweak-panel select{width:100%;padding:6px 8px;border:1px solid #0a0a0a;font-family:inherit;font-size:13px;background:#fff}
        #tweak-panel .tp-sec-grid{display:grid;grid-template-columns:1fr 1fr;gap:6px;max-height:200px;overflow:auto;padding:8px;background:#f4f4f4;border:1px solid #d0d0d0}
        #tweak-panel .tp-sec{display:flex;gap:6px;align-items:center;font-size:11px}
        #tweak-panel h4{font-family:'Gmarket Sans',sans-serif;font-size:12px;font-weight:700;letter-spacing:0.05em;text-transform:uppercase;color:#0a0a0a;border-bottom:1px solid #0a0a0a;padding-bottom:4px}
        #tweak-panel button.tp-btn{padding:8px;border:2px solid #0a0a0a;background:#fff;font-family:inherit;font-size:11px;cursor:pointer;margin-top:6px}
      </style>
      <h3>Tweaks <button class="tp-close">×</button></h3>
      <div class="tp-body">
        <div class="tp-group">
          <h4>Accent Preset</h4>
          <div class="tp-presets">
            <button class="tp-preset" style="background:oklch(0.58 0.22 28)" data-preset="ember"></button>
            <button class="tp-preset" style="background:oklch(0.52 0.14 145)" data-preset="forest"></button>
            <button class="tp-preset" style="background:oklch(0.55 0.18 250)" data-preset="cobalt"></button>
            <button class="tp-preset" style="background:oklch(0.72 0.17 70)" data-preset="amber"></button>
            <button class="tp-preset" style="background:#333" data-preset="mono"></button>
          </div>
        </div>
        <div class="tp-group">
          <label>Hue <span data-v="accentHue">${state.accentHue}</span></label>
          <input type="range" min="0" max="360" step="1" value="${state.accentHue}" data-k="accentHue">
          <label>Chroma <span data-v="accentChroma">${state.accentChroma}</span></label>
          <input type="range" min="0" max="0.3" step="0.01" value="${state.accentChroma}" data-k="accentChroma">
          <label>Lightness <span data-v="accentLight">${state.accentLight}</span></label>
          <input type="range" min="0.3" max="0.85" step="0.01" value="${state.accentLight}" data-k="accentLight">
        </div>
        <div class="tp-group">
          <h4>Typography</h4>
          <label>Display</label>
          <select data-k="displayFont"><option>Gmarket Sans</option><option>Pretendard</option></select>
          <label>Body</label>
          <select data-k="bodyFont"><option>Pretendard</option><option>Gmarket Sans</option></select>
        </div>
        <div class="tp-group">
          <h4>Layout</h4>
          <label>Density <span data-v="density">${state.density}</span></label>
          <input type="range" min="0.5" max="1.4" step="0.05" value="${state.density}" data-k="density">
          <label>Container <span data-v="containerWidth">${state.containerWidth}px</span></label>
          <input type="range" min="860" max="1400" step="20" value="${state.containerWidth}" data-k="containerWidth">
          <label>Display 줄간격 <span data-v="lhDisplay">${state.lhDisplay}</span></label>
          <input type="range" min="0.9" max="1.6" step="0.05" value="${state.lhDisplay}" data-k="lhDisplay">
          <label>Body 줄간격 <span data-v="lhBody">${state.lhBody}</span></label>
          <input type="range" min="1.3" max="2.0" step="0.05" value="${state.lhBody}" data-k="lhBody">
        </div>
        <div class="tp-group">
          <h4>Sections</h4>
          <div class="tp-sec-grid" id="tp-sections"></div>
          <button class="tp-btn" id="tp-reorder">Shuffle Order</button>
          <button class="tp-btn" id="tp-reset-order">Reset Order</button>
        </div>
      </div>`;
    document.body.appendChild(panel);

    const LABELS = {hero:'01 Hero',statement:'02 Statement',pain:'03 Pain',solution:'04 Solution',hook:'05 Hook',usp:'06 USP',featSplit:'07 Feat Split',featStrip:'08 Feat Strip',info:'09 Info',ing:'10 Ingredient',howto:'11 How-to',scene:'12 Scene',ba:'13 B/A',compare:'14 Compare',reviews:'15 Reviews',quote:'16 Quote',timeline:'17 Timeline',bstory:'18 Brand',faq:'19 FAQ',cta:'20 CTA'};
    const sw = panel.querySelector('#tp-sections');
    Object.entries(LABELS).forEach(([k,v])=>{ const d=document.createElement('label'); d.className='tp-sec'; d.innerHTML=`<input type="checkbox" ${state.sectionsOn[k]?'checked':''} data-sec-toggle="${k}"> <span>${v}</span>`; sw.appendChild(d); });
    panel.querySelector('[data-k="displayFont"]').value = state.displayFont;
    panel.querySelector('[data-k="bodyFont"]').value = state.bodyFont;

    panel.addEventListener('input', onChange);
    panel.addEventListener('change', onChange);
    panel.addEventListener('click', (e)=>{
      const p = e.target.closest('[data-preset]');
      if (p){ Object.assign(state, PRESETS[p.dataset.preset]); panel.querySelectorAll('[data-k]').forEach(el=>{ if (state[el.dataset.k]!==undefined) el.value=state[el.dataset.k]; const lab=panel.querySelector(`[data-v="${el.dataset.k}"]`); if(lab) lab.textContent=state[el.dataset.k]; }); apply(); post(); }
      if (e.target.closest('.tp-close')) hide();
      if (e.target.id==='tp-reorder') shuffle();
      if (e.target.id==='tp-reset-order') reset();
    });
    mounted = true;
  }
  function onChange(e){
    const t = e.target;
    if (t.dataset.k){ let v=t.value; if(t.type==='range') v=Number(v); state[t.dataset.k]=v; const lab=panel.querySelector(`[data-v="${t.dataset.k}"]`); if(lab) lab.textContent = t.dataset.k==='containerWidth'?v+'px':v; apply(); post(); }
    if (t.dataset.secToggle){ state.sectionsOn[t.dataset.secToggle]=t.checked; apply(); post(); }
  }
  function shuffle(){ const m=document.querySelector('main'); if(!m) return; const secs=Array.from(m.querySelectorAll('[data-sec]')); const hero=secs.find(s=>s.dataset.sec==='hero'); const cta=secs.find(s=>s.dataset.sec==='cta'); const mid=secs.filter(s=>s.dataset.sec!=='hero'&&s.dataset.sec!=='cta'); for(let i=mid.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[mid[i],mid[j]]=[mid[j],mid[i]];} [hero,...mid,cta].filter(Boolean).forEach(el=>m.appendChild(el)); }
  function reset(){ const m=document.querySelector('main'); if(!m) return; const secs=Array.from(m.querySelectorAll('[data-sec]')); secs.sort((a,b)=>(+a.dataset.order)-(+b.dataset.order)); secs.forEach(el=>m.appendChild(el)); }
  function post(){ try{ window.parent.postMessage({type:'__edit_mode_set_keys', edits:state}, '*'); }catch(e){} }
  function show(){ build(); panel.style.display=''; }
  function hide(){ if(panel) panel.style.display='none'; }
  window.addEventListener('message',(e)=>{ const d=e.data||{}; if(d.type==='__activate_edit_mode') show(); if(d.type==='__deactivate_edit_mode') hide(); });
  try{ window.parent.postMessage({type:'__edit_mode_available'}, '*'); }catch(e){}
})();

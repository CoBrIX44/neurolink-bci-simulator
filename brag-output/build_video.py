"""Create a local Hyperframes composition using verified synthetic project data."""
from pathlib import Path
import json
import html

OUT = Path(__file__).resolve().parent
COMP = OUT / 'composition'
data = json.loads((OUT.parent / 'presentation/signal_examples.json').read_text())['left']
audio = json.loads((COMP / 'assets/music/audio-data.json').read_text())

def trace(values, width=1080, height=275):
    return ' '.join(f'{i/(len(values)-1)*width:.2f},{height/2-v*height/8:.2f}' for i,v in enumerate(values))

def graph(prefix, width=1080, height=275):
    grid = ''.join(f'<line x1="0" y1="{y}" x2="{width}" y2="{y}" stroke="#DCE5E7" stroke-width="1"/>' for y in (30, height/2, height-30))
    return f'''<svg viewBox="-3 -3 {width+6} {height+6}" width="{width}" height="{height}" aria-label="Actual synthetic seed 7 waveform">
    {grid}<g id="{prefix}-raw"><polyline points="{trace(data['raw'],width,height)}" fill="none" stroke="#8795A5" stroke-width="2.5" stroke-dasharray="4 5"/></g>
    <g id="{prefix}-filtered"><polyline points="{trace(data['filtered'],width,height)}" fill="none" stroke="#087E8B" stroke-width="4" stroke-linejoin="round"/></g></svg>'''

low=data['features']['mean_power_1_12_hz']
high=data['features']['mean_power_12_40_hz']
automation=html.escape(json.dumps({'version':1,'lanes':[{'target':'volume','points':[{'t':0,'v':0},{'t':.6,'v':.30},{'t':20.5,'v':.30},{'t':22,'v':0}]}]}),quote=True)
page='''<!doctype html><html lang="en"><head><meta charset="UTF-8"><title>NeuroLink — From signal to command</title>
<script src="assets/gsap.min.js"></script><style>
@font-face{font-family:NeuroSans;src:url('assets/fonts/segoeui.ttf')} @font-face{font-family:NeuroSans;src:url('assets/fonts/segoeuib.ttf');font-weight:700}
*{box-sizing:border-box}body{margin:0;background:#F4F7F7;color:#16313B;font-family:NeuroSans,sans-serif}#root{position:relative;width:100%;height:100%;overflow:hidden;background:#F4F7F7}
.clip{position:absolute;inset:0}.grid{position:absolute;inset:0;background-image:linear-gradient(#087e8b12 1px,transparent 1px),linear-gradient(90deg,#087e8b12 1px,transparent 1px);background-size:80px 80px;opacity:.6}
.top{position:absolute;left:92px;right:92px;top:52px;display:flex;align-items:center;justify-content:space-between;z-index:20}.wordmark{font-size:30px;font-weight:700;letter-spacing:-1px}.badge{font-size:25px;color:#075D67;background:#E1F1F2;border:2px solid #A2CDD1;border-radius:30px;padding:10px 24px}.foot{position:absolute;bottom:38px;left:92px;font-size:23px;color:#49636A;z-index:20}.progress{position:absolute;bottom:0;left:0;width:100%;height:7px;background:#087E8B;transform-origin:left;z-index:25}
.hook-inner{position:absolute;inset:0}.eyebrow{font-size:25px;letter-spacing:4px;text-transform:uppercase;color:#087E8B;font-weight:700}.hookcopy{position:absolute;left:120px;top:215px}.hookcopy h1{font-size:112px;line-height:1.1;letter-spacing:-5px;margin:25px 0}.hookcopy p{font-size:38px;margin:20px 0}.hookgraph{position:absolute;left:120px;top:590px;width:1680px;height:300px}.hooklabel{position:absolute;right:130px;top:910px;font-size:25px;color:#49636A}
.scene-title{position:absolute;left:110px;top:140px;font-size:52px;letter-spacing:-1.5px;font-weight:700}.board{position:absolute;left:110px;top:235px;width:1700px;height:735px;background:#fff;border:2px solid #CADBDD;border-radius:20px;box-shadow:0 18px 45px #16313b15;overflow:hidden}.board-title{height:85px;padding:20px 35px;border-bottom:2px solid #DCE5E7;font-size:31px;font-weight:700}.board-title span{font-size:22px;color:#49636A;font-weight:400;margin-left:24px}.sidebar{position:absolute;left:0;top:85px;width:340px;bottom:0;padding:35px 30px;background:#EAF1F2;border-right:2px solid #DCE5E7}.sidebar h3{font-size:28px;line-height:1.25;margin:0 0 30px}.label{font-size:23px;color:#324E57;margin:21px 0 12px}.field{height:57px;border:2px solid #B4C9CD;border-radius:9px;background:#fff;font-size:28px;padding:7px 17px}.field b{float:right;font-size:20px;margin-top:4px}.button{margin-top:31px;border-radius:9px;background:#087E8B;color:#fff;font-size:24px;text-align:center;padding:16px 5px;font-weight:700}.hint{font-size:22px;line-height:1.45;color:#49636A;margin-top:26px}.plot{position:absolute;left:380px;top:111px;width:1260px;height:390px}.plot-title{font-size:28px;font-weight:700}.legend{position:absolute;top:50px;left:2px;display:flex;gap:32px;font-size:22px;color:#49636A}.legend span{display:flex;gap:10px;align-items:center}.line{width:30px;border-top:4px solid #087E8B}.rawline{border-top:3px dotted #8795A5}.graph{position:absolute;left:55px;top:94px}.axis-y{position:absolute;left:0;top:74px;font-size:20px;color:#49636A}.axis-x{position:absolute;bottom:-5px;left:420px;font-size:20px;color:#49636A}.ticks{position:absolute;left:55px;right:125px;bottom:24px;display:flex;justify-content:space-between;font-size:20px;color:#49636A}.filter-tag{position:absolute;right:0;top:40px;color:#075D67;font-size:22px;padding:8px 13px;background:#E1F1F2;border-radius:7px}.empty{position:absolute;left:495px;top:270px;font-size:28px;color:#49636A;background:#fff;padding:25px}.resultrow{position:absolute;left:380px;top:535px;width:1260px;height:172px;display:flex;gap:30px}.features{width:755px;border-top:2px solid #CADBDD;padding-top:14px}.features h3{font-size:26px;margin:0 0 11px}.feature-values{display:flex;gap:46px}.feature-name{font-size:22px;color:#49636A}.feature-value{font-size:43px;font-weight:700;color:#087E8B}.units{font-size:19px;color:#49636A}.prediction{width:460px;background:#E1F1F2;border:2px solid #A2CDD1;border-radius:12px;padding:16px 24px}.prediction-label{font-size:24px;color:#075D67}.prediction-value{font-size:62px;line-height:1.1;font-weight:700;color:#075D67}.pointer{position:absolute;left:0;top:0;width:44px;height:55px;z-index:8}.intro-tag{position:absolute;left:610px;top:783px;font-size:34px;color:#075D67}.outro-content{position:absolute;left:120px;top:250px;width:1680px}.outro-content h1{font-size:150px;letter-spacing:-7px;line-height:1.1;margin:24px 0 0}.outro-content h2{font-size:54px;letter-spacing:-1px;font-weight:400;margin:20px 0}.outro-team{font-size:30px;margin-top:42px;color:#49636A}.outro-wave{position:absolute;left:960px;top:335px;width:790px;height:310px}.rule{position:absolute;left:120px;right:120px;top:820px;height:3px;background:#AAC9CD}.end-note{position:absolute;left:120px;top:855px;font-size:29px;color:#49636A}
</style></head><body><div id="root" data-composition-id="neurolink" data-start="0" data-duration="22" data-width="1920" data-height="1080">
<div class="grid" id="ambient" data-layout-ignore></div>
<div class="top"><div class="wordmark">NeuroLink</div><div class="badge">Synthetic signals only · No real EEG</div></div>
<div class="foot">TEAM 2 / EXPERIENTIAL LEARNING</div><div class="progress" id="progress"></div>
<section class="clip" id="hook" data-start="0" data-duration="3" data-track-index="0"><div class="hook-inner">
<div class="hookcopy"><div class="eyebrow">See the pipeline</div><h1>From signal to command.</h1><p>A hands-on BCI simulator.</p></div>
<div class="hookgraph">__HOOKGRAPH__</div><div class="hooklabel">Generated waveform · 512 samples</div></div></section>
<section class="clip" id="demo" data-start="3" data-duration="15.56" data-track-index="1"><div id="demo-inner">
<div class="scene-title" id="title-reveal">NeuroLink — BCI Simulator</div>
<div class="scene-title" id="title-flow">Generate. Filter. Explore.</div>
<div class="scene-title" id="title-result">Features → artificial output</div>
<div class="board" id="board"><div class="board-title">NeuroLink <span>Synthetic educational lab · 256 Hz · 2 seconds</span></div>
<div class="sidebar"><h3>Generate a synthetic example</h3><div class="label">Artificial signal class</div><div class="field">left <b>⌄</b></div><div class="label">Reproducible signal seed</div><div class="field">7</div><div class="button" id="generate">Generate and process</div><p class="hint">The selected class controls the generator.</p></div>
<div class="plot"><div class="plot-title">Raw and filtered synthetic waveforms</div><div class="legend"><span><i class="line rawline"></i>Raw</span><span id="filtered-legend"><i class="line"></i>Filtered</span></div><div class="filter-tag" id="filter-tag">1–40 Hz · offline filter</div><div class="axis-y">Amplitude (arbitrary units)</div><div class="graph">__GRAPH__</div><div class="ticks"><span>0.0</span><span>0.5</span><span>1.0</span><span>1.5</span><span>2.0</span></div><div class="axis-x">Time (seconds)</div></div>
<div class="empty" id="empty">Choose an artificial class. Generate an example.</div>
<div class="resultrow"><div class="features" id="features"><h3>Named spectral features</h3><div class="feature-values"><div><div class="feature-name">Mean power · [1, 12) Hz</div><div class="feature-value">__LOW__</div></div><div><div class="feature-name">Mean power · [12, 40] Hz</div><div class="feature-value">__HIGH__</div></div></div><div class="units">Arbitrary amplitude² · mean per FFT bin</div></div><div class="prediction" id="prediction"><div class="prediction-label">Predicted demo command</div><div class="prediction-value">← left</div><div class="units">Artificial label · seed 7</div></div></div>
<svg class="pointer" id="pointer" viewBox="0 0 44 55"><path d="M3 3 L3 43 L14 34 L23 51 L31 47 L22 30 L37 29 Z" fill="#16313B" stroke="#fff" stroke-width="3"/></svg>
</div></div></section>
<section class="clip" id="outro" data-start="18.56" data-duration="3.44" data-track-index="2"><div id="outro-inner"><div class="outro-content"><div class="eyebrow">Build. Observe. Understand.</div><h1>NeuroLink</h1><h2>Explore the pipeline.</h2><div class="outro-team">Built by Team 2</div></div><div class="outro-wave">__OUTROGRAPH__</div><div class="rule"></div><div class="end-note">An educational BCI simulator, powered by synthetic signals.</div></div></section>
<audio id="music" src="assets/music/bed.mp3" data-start="0" data-duration="22" data-track-index="10" data-volume="0.3" data-automation="__AUTOMATION__"></audio>
<audio id="reveal-sfx" src="assets/sfx/impactSoft_medium_001.ogg" data-start="3" data-duration="0.18" data-track-index="11" data-volume="0.45"></audio>
<audio id="click-sfx" src="assets/sfx/click2.ogg" data-start="6" data-duration="0.06" data-track-index="12" data-volume="0.55"></audio>
<audio id="result-sfx" src="assets/sfx/impactSoft_medium_004.ogg" data-start="13.11" data-duration="0.15" data-track-index="13" data-volume="0.45"></audio>
</div><script>
const tl=gsap.timeline({paused:true});
tl.fromTo('#progress',{scaleX:0},{scaleX:1,duration:22,ease:'none'},0);
tl.fromTo('.hookcopy',{y:32,opacity:0},{y:0,opacity:1,duration:.5,ease:'power3.out'},0);
tl.fromTo('#hook-raw',{clipPath:'inset(0 100% 0 0)'},{clipPath:'inset(0 0% 0 0)',duration:1.6,ease:'none'},.15);
tl.set('#hook-filtered',{opacity:0},0);
tl.fromTo('.hooklabel',{opacity:0},{opacity:1,duration:.4},.6);
tl.to('.hook-inner',{y:-35,opacity:0,duration:.25,ease:'power2.in'},2.75);
tl.fromTo('#demo-inner',{y:70,opacity:0},{y:0,opacity:1,duration:.55,ease:'power3.out'},3);
tl.fromTo('#title-reveal',{opacity:1},{opacity:0,duration:.2},5.75);
tl.fromTo('#title-flow',{opacity:0},{opacity:1,duration:.25},6);
tl.to('#title-flow',{opacity:0,duration:.2},12.85);
tl.fromTo('#title-result',{opacity:0},{opacity:1,duration:.25},13.11);
tl.fromTo('#pointer',{x:490,y:590,opacity:0},{x:210,y:506,opacity:1,duration:.75,ease:'power2.inOut'},5.1);
tl.fromTo('#generate',{scale:1},{scale:.96,duration:.09,yoyo:true,repeat:1,ease:'power1.inOut'},6);
tl.to('#pointer',{opacity:0,duration:.2},6.3);
tl.to('#empty',{opacity:0,duration:.15},6);
tl.fromTo('#plot-raw',{clipPath:'inset(0 100% 0 0)'},{clipPath:'inset(0 0% 0 0)',duration:1.8,ease:'none'},6.1);
// beat-locked: filtered signal at 8.74s; scientific values never react to music.
tl.fromTo('#plot-filtered',{clipPath:'inset(0 100% 0 0)'},{clipPath:'inset(0 0% 0 0)',duration:1.4,ease:'power1.inOut'},8.74);
tl.fromTo('#filter-tag, #filtered-legend',{opacity:0},{opacity:1,duration:.35},8.74);
// beat-locked: result at 13.11s. Features and result hold together for legibility.
tl.fromTo('#features',{y:25,opacity:0},{y:0,opacity:1,duration:.45,ease:'power3.out'},13.11);
tl.fromTo('#prediction',{x:25,opacity:0},{x:0,opacity:1,duration:.45,ease:'power2.out'},13.11);
tl.to('#demo-inner',{opacity:0,y:-25,duration:.26},18.3);
// beat-locked: final identity at 18.56s.
tl.fromTo('#outro-inner',{opacity:0,y:24},{opacity:1,y:0,duration:.5,ease:'power3.out'},18.56);
tl.set('#outro-raw',{opacity:0},0);
tl.fromTo('#outro-filtered',{clipPath:'inset(0 100% 0 0)'},{clipPath:'inset(0 0% 0 0)',duration:1.1,ease:'power2.out'},18.56);
const AUDIO=__AUDIO__;
for(let f=0;f<660;f++){const amp=AUDIO.frames[f].rms ?? AUDIO.frames[f].bands[0];tl.set('#ambient',{opacity:.35+.25*amp},f/30);}
window.__timelines=window.__timelines||{};window.__timelines['neurolink']=tl;
</script></body></html>'''
page=page.replace('__HOOKGRAPH__',graph('hook',1680,300)).replace('__GRAPH__',graph('plot')).replace('__OUTROGRAPH__',graph('outro',790,310))
page=page.replace('__LOW__',f'{low:.4f}').replace('__HIGH__',f'{high:.4f}').replace('__AUTOMATION__',automation).replace('__AUDIO__',json.dumps({'frames':audio['frames'][:660]},separators=(',',':')))
(COMP/'index.html').write_text(page,encoding='utf-8')
(COMP/'index.motion.json').write_text(json.dumps({'duration':22,'assertions':[{'kind':'appearsBy','selector':'.hookcopy','bySec':.6},{'kind':'appearsBy','selector':'#prediction','bySec':13.8},{'kind':'staysInFrame','selector':'.badge'}]},indent=2))
(OUT/'share-copy.txt').write_text('We built NeuroLink: a hands-on BCI simulator that takes synthetic signals through filtering, feature extraction and classification. Explore the pipeline in an interactive dashboard—educational simulation only, with no real EEG or thought-reading.\n',encoding='utf-8')
print(f'Created {COMP / "index.html"}')


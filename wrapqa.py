import asyncio,sys,os,json
from playwright.async_api import async_playwright
S=sys.argv[1:] or sorted(l for l in os.listdir('.') if os.path.isfile(l+'/index.html'))
J='''()=>{const q='nav a,nav b,nav strong,header nav *,.btn,button,a[href^="tel:"],[class*=logo],[class*=brand],.mk-bar a,.mk-bar button';const bad=[];
document.querySelectorAll(q).forEach(e=>{if(e.closest('.mk-st,.mk-sheet,.mk-ring'))return;const r=e.getBoundingClientRect();if(!r.width||!r.height)return;const cs=getComputedStyle(e);if(cs.visibility=='hidden'||+cs.opacity==0)return;const t=e.innerText&&e.innerText.trim();if(!t||t.length>48)return;
const fs=parseFloat(cs.fontSize);let lh=parseFloat(cs.lineHeight);if(isNaN(lh))lh=fs*1.3;
// measure text lines via range
const rs=[];const tw=document.createTreeWalker(e,NodeFilter.SHOW_TEXT);let n;while(n=tw.nextNode()){if(!n.textContent.trim())continue;const rg=document.createRange();rg.selectNodeContents(n);rs.push(...[...rg.getClientRects()].filter(x=>x.width>1))}const tops=new Set(rs.map(x=>Math.round(x.top/4)));
if(tops.size>1&&!e.matches('.mk-bar a,.mk-bar button'))bad.push(e.tagName+'.'+(e.className+'').slice(0,20)+':'+t.replace(/\\s+/g,' ').slice(0,30)+' lines='+tops.size);
if(r.right>innerWidth+1&&cs.position!='fixed')bad.push('OUT:'+t.slice(0,25))});
return {bad:[...new Set(bad)].slice(0,8),sw:document.documentElement.scrollWidth,vw:innerWidth}}'''
async def main():
    async with async_playwright() as pw:
        wk=await pw.webkit.launch();dev=pw.devices['iPhone 14'];out={}
        for w in (375,390):
            c=await wk.new_context(**{**dev,'viewport':{'width':w,'height':812 if w==375 else 844}})
            for s in S:
                p=await c.new_page();errs=[];p.on('pageerror',lambda e:errs.append(str(e)[:90]))
                await p.goto(f'http://127.0.0.1:8765/{s}/index.html',wait_until='load',timeout=45000);await p.wait_for_timeout(1500)
                r=await p.evaluate(J);r['err']=errs
                await p.evaluate('scrollTo(0,innerHeight*1.2)');await p.wait_for_timeout(900)
                r2=await p.evaluate(J);r['bad']=list(dict.fromkeys(r['bad']+r2['bad']));r['bar']=await p.evaluate("!!document.querySelector('.mk-bar.on')")
                if w==390:await p.screenshot(path=f'_shots/{s}_bar.png')
                out.setdefault(s,{})[w]=r;await p.close()
            await c.close()
        for s,v in out.items():
            flag=any(v[w]['bad'] or v[w]['sw']>v[w]['vw'] or v[w]['err'] or not v[w]['bar'] for w in v)
            print(('!! ' if flag else 'ok ')+s,json.dumps({w:{k:v[w][k] for k in ('bad','err','bar') if v[w][k] or k=='bar'} for w in v},ensure_ascii=False) if flag else '')
asyncio.run(main())

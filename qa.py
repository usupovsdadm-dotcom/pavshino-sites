import asyncio,sys,json
from playwright.async_api import async_playwright
S=sys.argv[1:] or [l for l in __import__('os').listdir('.') if __import__('os').path.isfile(l+'/index.html')]
CHK='''()=>{const out={};out.sw=document.documentElement.scrollWidth;out.vw=innerWidth;
out.hidden=[...document.querySelectorAll('body *')].filter(e=>{if(e.closest('.intro,canvas,svg,#cur,.cloud,.leaf,.star,.card,.ring,.tail,.bk,.paws'))return false;const r=e.getBoundingClientRect();if(r.width<4||r.height<4)return false;if(!e.textContent.trim()&&e.tagName!='IMG')return false;let o=1,n=e;while(n&&n!==document.body){const cs=getComputedStyle(n);o*=+cs.opacity;if(cs.visibility=='hidden')o=0;n=n.parentElement}return o<.3}).map(e=>e.tagName+'.'+e.className+':'+e.textContent.trim().slice(0,30)).slice(0,8);
out.badimg=[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src.split('/').pop());
out.empty=[...document.querySelectorAll('[data-count],[data-c]')].filter(e=>!e.textContent.trim()||e.textContent.trim()=='0'&&+ (e.dataset.count||e.dataset.c)>0).map(e=>e.outerHTML.slice(0,60));
out.wide=[...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.right>innerWidth+2&&r.width>0&&!e.closest('.marquee,.strip,.ticker,.flow,.track,.sl,.hz,.mq-in,canvas,.hole')&&getComputedStyle(e).position!='fixed'}).map(e=>e.tagName+'.'+e.className).slice(0,5);
return out}'''
async def run(br,ctxargs,s,tag):
    c=await br.new_context(**ctxargs);p=await c.new_page();errs=[]
    p.on('pageerror',lambda e:errs.append('JS:'+str(e)[:100]));p.on('requestfailed',lambda r:errs.append('REQ:'+r.url[:90]))
    await p.goto(f'http://127.0.0.1:8765/{s}/index.html',wait_until='domcontentloaded',timeout=45000);await p.wait_for_timeout(3000)
    h=await p.evaluate('document.documentElement.scrollHeight')
    y=0
    while y<h: y+=500;await p.evaluate(f'scrollTo(0,{y})');await p.wait_for_timeout(120);h=await p.evaluate('document.documentElement.scrollHeight')
    await p.wait_for_timeout(1800)
    # check at each viewport position again for hidden
    res={'hidden':set(),'wide':set()};o=None
    for yy in range(0,h,int(ctxargs['viewport']['height']*0.9)):
        await p.evaluate(f'scrollTo(0,{yy})');await p.wait_for_timeout(900)
        o=await p.evaluate(CHK.replace("const r=e.getBoundingClientRect();if(r.width<4","const r=e.getBoundingClientRect();if(r.bottom<0||r.top>innerHeight)return false;if(r.width<4"))
        res['hidden']|=set(o['hidden']);res['wide']|=set(o['wide'])
    await p.screenshot(path=f'_shots/{s}_{tag}_qa.png')
    await c.close()
    errs=[e for e in errs if 'yandex' not in e and 'fonts.g' not in e]
    return dict(sw=o['sw'],vw=o['vw'],hidden=sorted(res['hidden']),wide=sorted(res['wide']),badimg=o['badimg'],empty=o['empty'],errs=errs[:5])
async def main():
    async with async_playwright() as pw:
        wk=await pw.webkit.launch();ch=await pw.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        ip=pw.devices['iPhone 14']
        R={}
        for s in sorted(S):
            a,b=await asyncio.gather(run(wk,dict(ip),s,'ios'),run(ch,dict(viewport={'width':1440,'height':900}),s,'desk'))
            R[s]={'ios':a,'desk':b}
            bad={k:{x:y for x,y in v.items() if y and x not in('sw','vw')} for k,v in R[s].items()}
            for k in bad:
                if R[s][k]['sw']>R[s][k]['vw']:bad[k]['overflow']=R[s][k]['sw']
            print(s,json.dumps(bad,ensure_ascii=False),flush=True)
        json.dump(R,open('_qa.json','w'),ensure_ascii=False,indent=1)
asyncio.run(main())

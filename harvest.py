import asyncio,json,re
from playwright.async_api import async_playwright
M=json.load(open('_raw/meta.json'))
async def rev(b,m):
    p=await b.new_page(locale='ru-RU')
    try:
        await p.goto(f"https://2gis.ru/krasnogorsk/firm/{m['fid']}/tab/reviews",timeout=40000,wait_until='domcontentloaded');await p.wait_for_timeout(5000)
        t=await p.evaluate('''()=>[...document.querySelectorAll('a._co8kyiw,a[class*="_1msln3t"],div._49x36f a')].map(a=>{let c=a.closest('div[class]');for(let k=0;k<6&&c;k++)c=c.parentElement;return {t:a.innerText.trim(),ctx:c?c.innerText.slice(0,200):''}}).filter(x=>x.t.length>30)''')
    except Exception as e: t=[{'err':str(e)[:80]}]
    await p.close();return t
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for k in range(0,len(M),4):
            rs=await asyncio.gather(*[rev(b,m) for m in M[k:k+4]])
            for m,r in zip(M[k:k+4],rs): m['reviews']=r[:8];print(m['i'],m['name'],len(r),(r[0].get('t','')[:80] if r else ''))
        await b.close()
    json.dump(M,open('_raw/meta.json','w'),ensure_ascii=False)
asyncio.run(main())

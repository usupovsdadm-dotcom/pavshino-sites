import asyncio,json,re
from playwright.async_api import async_playwright
U={14:['https://taplink.cc/barlondon'],12:['https://dikidi.net/g374846'],24:['https://dikidi.ru/815366','http://ucynayuliya.ru'],27:['https://dikidi.ru/1569600'],15:['http://widget.sonline.su/ru/services/?placeid=269937878'],26:['http://gruzinskie-kanikuli.ru'],25:['https://yourmed.clinic/filials/krasnogorsk/'],1:['http://autopoyma.ru'],13:['https://taplink.cc/pink_code']}
async def get(b,u):
    p=await b.new_page(locale='ru-RU',user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36')
    try:
        await p.goto(u,timeout=40000,wait_until='domcontentloaded');await p.wait_for_timeout(7000)
        for _ in range(6): await p.mouse.wheel(0,2000);await p.wait_for_timeout(500)
        t=(await p.evaluate('document.body?document.body.innerText:""')) or ''
    except Exception as e: t='ERR '+str(e)[:80]
    await p.close();return t
async def main():
    R={}
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for i,us in U.items():
            for u in us:
                t=await get(b,u);open(f'_raw/{i:02d}/price_{abs(hash(u))%9999}.txt','w').write(u+'\n'+t)
                lines=[l for l in t.split('\n') if '₽' in l or 'руб' in l]
                print(i,u,len(t),len(lines),lines[:6])
        await b.close()
asyncio.run(main())

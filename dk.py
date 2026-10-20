import asyncio,sys
from playwright.async_api import async_playwright
J=[(27,'https://dikidi.ru/1569600'),(24,'https://dikidi.ru/815366'),(12,'https://dikidi.net/g374846'),(26,'https://gruzinskie-kanikuli.ru/'),(1,'https://autopoyma.ru/'),(13,'https://taplink.cc/pink_code'),(14,'https://taplink.cc/barlondon'),(15,'https://widget.sonline.su/ru/services/?placeid=269937878')]
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for i,u in J:
            p=await b.new_page(locale='ru-RU',viewport={'width':1300,'height':900})
            try:
                await p.goto(u,timeout=60000,wait_until='commit');await p.wait_for_timeout(9000)
                if i==12:
                    await p.click('text=Записаться',timeout=5000);await p.wait_for_timeout(5000)
                for t in ['Посмотреть все','Все услуги','Услуги','Меню']:
                    try: await p.click(f'text={t}',timeout=2500);await p.wait_for_timeout(4000);break
                    except: pass
                for _ in range(10): await p.mouse.wheel(0,2500);await p.wait_for_timeout(400)
                t=await p.evaluate('document.body?document.body.innerText:""')
            except Exception as e: t='ERR '+str(e)[:100]
            open(f'_raw/{i:02d}/full_{i}.txt','w').write(u+'\n'+(t or ''))
            print(i,u,len(t or ''),sum(1 for l in (t or '').split('\n') if 'RUB' in l or '₽' in l or 'руб' in l))
            await p.close()
        await b.close()
asyncio.run(main())

import asyncio,sys
from playwright.async_api import async_playwright
A=sys.argv[1:]
async def one(b,s,vw,vh,tag):
    p=await b.new_page(viewport={'width':vw,'height':vh},device_scale_factor=1)
    u=f'file:///workspace/pavshino_sites/{s}/index.html'
    await p.goto(u+'?shot',wait_until='domcontentloaded');await p.wait_for_timeout(2500)
    await p.screenshot(path=f'_shots/{s}_{tag}.png')
    await p.screenshot(path=f'_shots/{s}_{tag}_full.png',full_page=True)
    w=await p.evaluate('document.documentElement.scrollWidth')
    await p.close();return w
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for s in A:
            r=await asyncio.gather(one(b,s,390,844,'m'),one(b,s,1440,900,'d'))
            print(s,'scrollWidth m/d',r)
        await b.close()
asyncio.run(main())

import asyncio,sys
from playwright.async_api import async_playwright
S=sys.argv[1:]
async def main():
    async with async_playwright() as pw:
        wk=await pw.webkit.launch();c=await wk.new_context(**pw.devices['iPhone 14'])
        for s in S:
            p=await c.new_page();await p.goto(f'http://127.0.0.1:8765/{s}/index.html',wait_until='load');await p.wait_for_timeout(1800)
            await p.screenshot(path=f'_v/{s}_top.png')
            if await p.query_selector('.mk-ring'):
                await p.click('.mk-ring',force=True);await p.wait_for_timeout(1200);await p.screenshot(path=f'_v/{s}_st1.png')
                await p.mouse.click(350,400);await p.wait_for_timeout(900);await p.screenshot(path=f'_v/{s}_st2.png');await p.click('.mk-x',force=True);await p.wait_for_timeout(500)
            await p.evaluate('scrollTo(0,innerHeight*1.5)');await p.wait_for_timeout(900);await p.click('.mk-main',force=True);await p.wait_for_timeout(900);await p.screenshot(path=f'_v/{s}_sh.png')
            await p.close()
asyncio.run(main())

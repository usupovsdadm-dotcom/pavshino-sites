import re
from kit import *
S={0:('m-express','#101c38','#e8eef9','#e3262b',"'Russo One'",'0'),1:('autopoyma','#111','#f5f2ea','#f7c600',"Oswald",'0'),2:('gorilla','#0d0d0f','#ede6da','#c8a46a',"'Dela Gothic One'",'0'),3:('barberclub','#1b2b4a','#f2e8d8','#c9302c',"'Playfair Display'",'2px'),4:('zayushka','#fff','#2d3b2b','#e8793f',"Comfortaa",'32px'),5:('mary-poppins','#fffaf0','#2d2a3e','#a8323e',"'Yeseva One'",'0'),6:('pochemuchka','#fff','#1d2742','#3a6df0',"Unbounded",'28px'),7:('hvost','#fff','#2a1d20','#b4485c',"'Rubik Mono One'",'26px'),8:('belyi-krolik','#1a1820','#ece4d2','#c9a45c',"'Cinzel Decorative'",'0'),9:('coffee-flat','#fff','#1b1110','#e43b2c',"Unbounded",'24px'),10:('crush','#fbfbf7','#33402c','#9aa883',"Cormorant",'0'),11:('organika','#fff','#2f322d','#6b7a5a',"Marcellus",'40px'),12:('beauty-time','#2a201a','#f8f1e9','#d9c3a3',"'Bodoni Moda'",'0')}
for i,(slug,bg,fg,ac,fd,rad) in S.items():
    o=D[i];f=f'{slug}/index.html';t=open(f).read()
    # prices
    if i==3:
        tix=''.join(f'<div class="tk rv"><small>№ {k+1:02d}</small><h3>{E(a)}</h3><div class="p">{E(p)}</div></div>' for k,(a,p) in enumerate(o['prices'][:9]))
        t=re.sub(r'<div class="tix">.*?</div></section>',f'<div class="tix">{tix}</div><p style="text-align:center;margin-top:24px;opacity:.6;font-size:14px">Прайс — по данным barber-club.tilda.ws</p></section>',t,flags=re.S)
    if i==2:
        t=t.replace('<h3>Мужская стрижка</h3><b>от … ₽</b>','<h3>Мужская стрижка</h3><b>от 900 ₽</b>',1)
        t=t.replace('// прайс · цены — пример','// прайс · стоимость остальных услуг — при записи')
    t=re.sub(r'(<span class="pr">|<b>|<div class="p">|<span class="c">|<td>)от … ₽',r'\1по записи',t)
    t=t.replace('от … ₽','по записи').replace('~ … мин','')
    for a in ['<small>цена-пример</small>','<small>пример цены</small>',' <em>пример</em>','<p class="m" style="margin-top:12px">*цена — пример</p>']: t=t.replace(a,'')
    t=re.sub(r'<p[^>]*>[^<]*(?:Цены указаны для примера|цены указаны для примера|Цены — пример)[^<]*</p>','',t)
    t=re.sub(r'(<span[^>]*>)[^<]*(?:цены — пример|Цены — пример)[^<]*(</span>)',r'\1услуги и стоимость — уточняйте при записи\2',t)
    t=t.replace('Цены указаны для примера','Стоимость уточняйте при записи').replace('цены указаны для примера','стоимость уточняйте при записи')
    t=t.replace('Диагностика по записи*','Записаться на диагностику')
    # forms → WhatsApp
    t=re.sub(r'onsubmit="[^"]*"',form_attr(),t)
    t=re.sub(r'(<form[^>]*>.*?<button[^>]*>)([^<]*)(</button>)',lambda m:m.group(1)+btn_label(o)+m.group(3),t,flags=re.S)
    # info block
    revs=''.join(f'<figure class="xr-c"><div class="xr-s">★★★★★</div><blockquote>«{E(r["t"][:260]+("…" if len(r["t"])>260 else ""))}»</blockquote><figcaption>{E(r["n"])} · 2ГИС</figcaption></figure>' for r in o['reviews'])
    hrs=''.join(f'<li><span>{a}</span><b>{v}</b></li>' for a,v in hours_rows(o['hours']))
    blk=f'''<section class="xr" id="info"><style>.xr{{background:{bg};color:{fg};padding:clamp(60px,10vw,130px) 5vw}}.xr h2{{font-family:{fd},serif;font-size:clamp(34px,5vw,64px);line-height:1;margin:0 0 34px;color:{fg}}}.xr-g{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px}}.xr-c{{margin:0;padding:28px;border:1px solid {fg}22;border-radius:{rad};background:{fg}08;transition:transform .5s cubic-bezier(.2,.8,.2,1)}}.xr-c:hover{{transform:translateY(-6px)}}.xr-s{{color:{ac};letter-spacing:3px}}.xr blockquote{{margin:14px 0;font-size:17px;line-height:1.55}}.xr figcaption{{opacity:.6;font-size:14px}}.xr-b{{display:grid;grid-template-columns:1fr 1fr;gap:5vw;margin-top:clamp(50px,8vw,100px)}}.xr ul{{list-style:none;padding:0;margin:0}}.xr li{{display:flex;justify-content:space-between;padding:14px 0;border-bottom:1px solid {fg}22;font-size:18px}}.xr-so{{display:flex;flex-wrap:wrap;gap:10px}}.xr-so a{{padding:12px 20px;border:1px solid {fg}44;border-radius:{rad if rad!='0' else '0'};text-decoration:none;color:{fg};transition:.3s}}.xr-so a:hover{{background:{ac};border-color:{ac};color:{bg}}}@media(max-width:760px){{.xr-b{{grid-template-columns:1fr}}}}</style>
{f'<h2>Отзывы гостей</h2><div class="xr-g">{revs}</div>' if revs else ''}<div class="xr-b"><div><h2>Часы работы</h2><ul>{hrs}</ul></div><div><h2>Мы на связи</h2><p style="font-size:20px;margin:0 0 20px"><a href="tel:{o['tel']}" style="color:{fg}">{E(o['phone'])}</a><br><span style="opacity:.7;font-size:16px">{E(o['addr'])}</span></p><div class="xr-so">{socials(o)}</div></div></div></section>'''
    t=re.sub(r'<section class="xr" id="info">.*?</section>','',t,flags=re.S)
    t=t.replace('<footer',blk+'\n<footer',1)
    if 'function waSend' not in t: t=t.replace('</body>',wa_js(o)+'</body>')
    open(f,'w').write(t);print(slug,t.count('по записи'),t.count('waSend'),bool(revs))

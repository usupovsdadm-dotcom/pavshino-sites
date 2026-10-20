import openpyxl,json,os,shutil,html,re
from PIL import Image
wb=openpyxl.load_workbook('/home/box/agent-data/agents/aa958351-6340-4885-82e6-1000b140a538/attachments/1cd8ea5767bb533182f091cdf31dc33391ab9083f9a303bf588b058802a2578c.xlsx')
rows=list(wb['Лиды Павшинская пойма'].iter_rows(values_only=True))[1:]
M=json.load(open('_raw/meta.json'))
E=html.escape
# slug, bg, fg, accent, accent2, display font, body font, hero, services, tagline, offer
C={
0:('m-express','#0e1a33','#eef2f8','#e3262b','#2f6bd8','Russo One','Manrope','full','table','Автосервис у дома в Павшинской пойме','Замена масла и диагностика — без очередей и сюрпризов в чеке'),
1:('autopoyma','#151515','#f3efe8','#f2b705','#c9c3b6','Oswald','Inter','split','cards','Автозапчасти и автотовары в пойме','Подберём деталь по VIN — заберите сегодня в пойме'),
2:('gorilla','#070809','#efe9df','#c8a46a','#5b5650','Bebas Neue','Manrope','neon','menu','Барбершоп в ЖК Прибрежный','Мужская стрижка, после которой хочется жить у зеркала'),
3:('barberclub','#14213a','#f4ede4','#c9302c','#f4ede4','Playfair Display','Inter','stack','menu','Барбершоп на Красногорском бульваре','Классика мужского груминга в клубной атмосфере'),
4:('zayushka','#fff8ee','#2c3b2a','#e2793f','#6e8f4e','Comfortaa','Nunito','card','tabs','Центр развития ребёнка','Игровые занятия, на которые малыши бегут сами'),
5:('mary-poppins','#f5f1ea','#2d2a3e','#b23a48','#2d2a3e','Cormorant Garamond','Nunito','stack','accordion','Школа для малышей','Бережный старт: первые шаги к школе — с заботой, как у Мэри Поппинс'),
6:('pochemuchka','#fdfbf4','#1f2f4a','#ffb703','#3a86ff','Unbounded','Nunito','canvas','cards','Студия раннего развития и логопед','Отвечаем на все «почему» — и ставим звуки играючи'),
7:('hvost','#f6e9ec','#2a1d20','#b4485c','#3e5a2e','Fraunces','Manrope','type','menu','Кафе-кофейня в ЖК ART','Завтраки, кофе и десерты, за которые ставят 5.0'),
8:('belyi-krolik','#121216','#ece6da','#c9a45c','#7a2e2e','Cormorant Garamond','Montserrat','canvas','menu','Кофейня на Красногорском бульваре','Спуститесь в нору: кофе, сад и немного волшебства'),
9:('coffee-flat','#1b1110','#f7ece4','#e43b2c','#f2c94c','Unbounded','Manrope','card','menu','Кофейня на Красногорском бульваре, 20','Кофе как у друга в квартире — только вкуснее'),
10:('crush','#eef1e6','#3c4a33','#8aa06b','#c7b89a','Cormorant Garamond','Jost','split','accordion','Beauty studio · брови и ресницы','Взгляд, в который влюбляются: брови и ресницы с рейтингом 4.9'),
11:('organika','#f3f0ea','#2f322d','#9a7b5f','#6b7a5a','Marcellus','Manrope','stack','table','Центр ногтевого сервиса','Чистый маникюр и педикюр в спокойной эко-эстетике'),
12:('beauty-time','#faf5ef','#3a2f26','#a8735d','#d9c6a8','Playfair Display','Jost','full','tabs','Студия красоты на Ильинском бульваре','Ваше время на красоту — без спешки'),
13:('pink-code','#ffb5e6','#000000','#000000','#ffffff','Montserrat','Montserrat','type','cards','Студия маникюра','Розовый код идеального маникюра'),
14:('london','#111418','#efe7dc','#b8312f','#1f3a5f','Abril Fatface','Inter','full','menu','Барбершоп на Молодёжной','Британская строгость, русская душевность'),
15:('sosedi','#efe8d8','#2b2420','#a3522f','#5b6b48','Rubik','Rubik','split','table','Мужская парикмахерская','Стригут как соседу — честно, аккуратно, рядом'),
16:('stefanny','#f4f1ec','#26221f','#8b5e3c','#c9b79c','Playfair Display','Manrope','stack','accordion','Ателье по ремонту одежды','Вернём любимой вещи посадку и жизнь'),
17:('mia','#eef3ee','#1e3328','#3f8f6b','#9ac3ad','Manrope','Manrope','canvas','table','Химчистка и чистка ковров','Ковры, шторы и одежда — как новые, с доставкой'),
18:('vsegda-kofe','#ffffff','#0b0b0b','#0b0b0b','#c5ad95','Oswald','Inter','type','menu','Кофейня на Красногорском бульваре','Всегда кофе. Всегда рядом. Всегда вовремя.'),
19:('495','#1d211a','#efeadf','#c4bc8d','#7d8a5a','Space Grotesk','Space Grotesk','split','cards','Кофейня на Красногорском бульваре, 18','Кофе на код 495 — по-московски быстро и вкусно'),
20:('prana','#f6f1e7','#3a2a17','#8f6a3f','#7c9a5c','Fraunces','Nunito','card','menu','Кофейня на Молодёжной','Кофе, который наполняет энергией — прана в чашке'),
21:('negrul','#f2efe8','#22252a','#3d6b4f','#d3a94a','Unbounded','Manrope','stack','menu','Кафе на Красногорском бульваре · вывеска «Эйфория»','Завтраки весь день — новое место в пойме'),
22:('popnails','#fdf3ee','#3a2219','#d9805f','#7c8a3b','Unbounded','Manrope','canvas','cards','Студия красоты','Сочный маникюр, который заметят все'),
23:('mindal','#f7efeb','#2b1e1f','#903335','#d6b9b1','Cormorant Garamond','Jost','type','table','Ногтевая студия','Нежность миндаля в каждом ноготке'),
24:('territoriya-manikyura','#fbf7f3','#3b2b25','#a37e71','#67463a','Marcellus','Manrope','split','tabs','Студия ногтевого сервиса · вход в N’ателье','Территория, где ногти в порядке'),
25:('yourmed','#f4f8fc','#11233d','#e8483f','#1e88e5','Manrope','Manrope','card','accordion','Медцентр для всей семьи в ЖК ART','Врачи для всей семьи — в соседнем доме'),
26:('gruzinskie-kanikuly','#1f2e22','#f3ead8','#c8743a','#d9b26a','Lobster','Nunito','full','menu','Ресторан домашней грузинской кухни','Хинкали, хачапури и тепло грузинского застолья'),
27:('lak-mi','#16070f','#fff1f6','#ff2f87','#3cff9a','Unbounded','Manrope','neon','cards','Студия маникюра на Молодёжной','Неоновый маникюр с характером — Лак Ми!'),
}
SV={
'Автосервис':[('Замена масла','от … ₽'),('Компьютерная диагностика','от … ₽'),('Тормозная система','от … ₽'),('Ходовая часть','от … ₽'),('Шиномонтаж','от … ₽'),('Электрика','от … ₽')],
'Автомагазин / запчасти':[('Подбор по VIN','от … ₽'),('Масла и жидкости','от … ₽'),('Фильтры','от … ₽'),('Тормозные колодки','от … ₽'),('Аккумуляторы','от … ₽'),('Автохимия','от … ₽')],
'barber':[('Мужская стрижка','от … ₽'),('Стрижка машинкой','от … ₽'),('Оформление бороды','от … ₽'),('Стрижка + борода','от … ₽'),('Детская стрижка','от … ₽'),('Королевское бритьё','от … ₽')],
'kids':[('Развивающие занятия 1–3 года','от … ₽'),('Подготовка к школе','от … ₽'),('Творческая мастерская','от … ₽'),('Музыка и движение','от … ₽'),('Пробное занятие','от … ₽'),('Абонемент','от … ₽')],
'logo':[('Занятия с логопедом','от … ₽'),('Раннее развитие','от … ₽'),('Подготовка к школе','от … ₽'),('Диагностика речи','от … ₽'),('Пробное занятие','от … ₽'),('Абонемент','от … ₽')],
'cafe':[('Капучино','от … ₽'),('Флэт уайт','от … ₽'),('Раф','от … ₽'),('Завтрак','от … ₽'),('Десерт','от … ₽'),('Кофе с собой','от … ₽')],
'rest':[('Хинкали','от … ₽'),('Хачапури по-аджарски','от … ₽'),('Пхали','от … ₽'),('Шашлык','от … ₽'),('Харчо','от … ₽'),('Лимонады','от … ₽')],
'brows':[('Архитектура бровей','от … ₽'),('Окрашивание бровей','от … ₽'),('Ламинирование бровей','от … ₽'),('Ламинирование ресниц','от … ₽'),('Наращивание ресниц','от … ₽'),('Комплекс «Взгляд»','от … ₽')],
'nails':[('Маникюр с покрытием','от … ₽'),('Маникюр без покрытия','от … ₽'),('Педикюр','от … ₽'),('Укрепление','от … ₽'),('Дизайн','от … ₽'),('Снятие','от … ₽')],
'beauty':[('Маникюр','от … ₽'),('Педикюр','от … ₽'),('Брови','от … ₽'),('Ресницы','от … ₽'),('Уход','от … ₽'),('Комплекс','от … ₽')],
'atelier':[('Подшив брюк и джинсов','от … ₽'),('Замена молнии','от … ₽'),('Ушив по фигуре','от … ₽'),('Ремонт верхней одежды','от … ₽'),('Ремонт кожи','от … ₽'),('Срочный ремонт','от … ₽')],
'clean':[('Чистка ковра, м²','от … ₽'),('Химчистка одежды','от … ₽'),('Шторы','от … ₽'),('Пуховики','от … ₽'),('Вызов курьера','от … ₽'),('Мягкая мебель','от … ₽')],
'med':[('Терапевт','от … ₽'),('Педиатр','от … ₽'),('Анализы','от … ₽'),('УЗИ','от … ₽'),('Справки','от … ₽'),('Вызов врача на дом','от … ₽')],
}
def kind(t,n):
    t=t.lower()
    if 'барбер' in t or 'парикмах' in t: return 'barber'
    if 'логопед' in t: return 'logo'
    if 'ребён' in t or 'малыш' in t: return 'kids'
    if 'ресторан' in t: return 'rest'
    if 'кофе' in t or 'кафе' in t: return 'cafe'
    if 'брови' in t: return 'brows'
    if 'ногт' in t or 'маникюр' in t: return 'nails'
    if 'красоты' in t: return 'beauty'
    if 'ателье' in t: return 'atelier'
    if 'химчист' in t: return 'clean'
    if 'мед' in t: return 'med'
    return t.capitalize() if False else ('Автосервис' if 'автосервис' in t else 'Автомагазин / запчасти')
SEC={'cafe':'Меню','rest':'Меню','kids':'Занятия','logo':'Занятия','Автомагазин / запчасти':'Каталог'}
GLY={'barber':'✂','cafe':'☕','rest':'🍷','kids':'★','logo':'✿','brows':'◉','nails':'✦','beauty':'✧','atelier':'✂','clean':'❋','med':'✚','Автосервис':'⚙','Автомагазин / запчасти':'⚙'}

def hero(v,c,d):
    n=E(d['name']);t=E(c[9]);o=E(c[10])
    cta=f'<div class="ctas"><a class="btn" href="#book">Записаться</a><a class="btn ghost" href="tel:{d["tel"]}">{E(d["phone"])}</a></div>'
    badge=f'<div class="rate"><b data-count="{d["r"]}">{d["rtxt"]}</b><span>★★★★★</span><small>{d["rsub"]}</small></div>'
    if v=='full': return f'<header class="h-full"><div class="bgimg" data-par="0.3" style="background-image:url(photo.jpg)"></div><div class="shade"></div><div class="wrap in"><p class="kicker rv">{t}</p><h1 class="split-t">{n}</h1><p class="lead rv">{o}</p>{cta}{badge}</div><div class="scrollhint">scroll</div></header>'
    if v=='split': return f'<header class="h-split wrap"><div class="in"><p class="kicker rv">{t}</p><h1 class="split-t">{n}</h1><p class="lead rv">{o}</p>{cta}{badge}</div><figure class="frame rv" data-tilt><img src="photo.jpg" alt="{n} — фото из 2ГИС"><span class="blob"></span></figure></header>'
    if v=='neon': return f'<header class="h-neon"><canvas id="fx"></canvas><div class="wrap in center"><p class="kicker rv">{t}</p><h1 class="neon split-t">{n}</h1><p class="lead rv">{o}</p>{cta}{badge}</div><img class="neonphoto" data-par="0.15" src="photo.jpg" alt=""></header>'
    if v=='type': return f'<header class="h-type"><div class="wrap"><p class="kicker rv">{t}</p><h1 class="giant split-t">{n}</h1><div class="h-row"><p class="lead rv">{o}</p><div class="circ rv" data-par="-0.1"><img src="photo.jpg" alt=""><svg viewBox="0 0 200 200" class="ring"><defs><path id="cp" d="M100,100 m-80,0 a80,80 0 1,1 160,0 a80,80 0 1,1 -160,0"/></defs><text><textPath href="#cp">{n} · {n} · {n} · {n} · </textPath></text></svg></div></div>{cta}{badge}</div></header>'
    if v=='canvas': return f'<header class="h-canvas"><canvas id="fx"></canvas><div class="wrap in center"><p class="kicker rv">{t}</p><h1 class="split-t">{n}</h1><p class="lead rv">{o}</p>{cta}{badge}<img class="float-photo rv" src="photo.jpg" alt="" data-par="-0.08"></div></header>'
    if v=='stack': return f'<header class="h-stack wrap"><div class="vert">{t}</div><div class="in"><p class="kicker rv">№ {d["no"]} · Павшинская пойма</p><h1 class="split-t">{n}</h1><p class="lead rv">{o}</p>{cta}{badge}</div><div class="tiles"><div class="tile t1 rv" data-par="0.06" style="background-image:url(photo.jpg)"></div><div class="tile t2 rv"><span>{GLY[d["k"]]}</span></div><div class="tile t3 rv" data-par="-0.06"><b>{d["rtxt"]}</b><small>2ГИС</small></div></div></header>'
    if v=='card': return f'<header class="h-card"><div class="mesh"></div><div class="wrap grid2"><div class="in"><p class="kicker rv">{t}</p><h1 class="split-t">{n}</h1><p class="lead rv">{o}</p>{cta}{badge}</div><div class="cards3"><div class="pc c1" data-tilt><img src="photo.jpg" alt=""></div><div class="pc c2" data-tilt>{d["logoimg"] or "<b>"+n+"</b>"}</div><div class="pc c3" data-tilt><b>{d["rtxt"]}</b><small>{d["rsub"]}</small></div></div></div></header>'

def services(v,items,title):
    note='<p class="note">Цены — пример-заглушка «от …». Реальный прайс подставим со слов владельца.</p>'
    if v=='cards': b=''.join(f'<article class="sc rv" data-tilt><span class="num">{i+1:02d}</span><h3>{E(a)}</h3><p class="pr">{p} <em>пример</em></p></article>' for i,(a,p) in enumerate(items)); return f'<div class="sgrid">{b}</div>{note}'
    if v=='menu': b=''.join(f'<li class="rv"><span>{E(a)}</span><i></i><b>{p}</b></li>' for a,p in items); return f'<ul class="menu">{b}</ul>{note}'
    if v=='table': b=''.join(f'<tr class="rv"><td>{i+1:02d}</td><td>{E(a)}</td><td>{p}</td></tr>' for i,(a,p) in enumerate(items)); return f'<table class="ptab"><thead><tr><th>№</th><th>Услуга</th><th>Цена (пример)</th></tr></thead><tbody>{b}</tbody></table>{note}'
    if v=='accordion': b=''.join(f'<details class="rv" {"open" if i==0 else ""}><summary>{E(a)}<b>{p}</b></summary><p>Описание услуги заполним вместе с мастером. Цена — пример.</p></details>' for i,(a,p) in enumerate(items)); return f'<div class="acc">{b}</div>{note}'
    if v=='tabs':
        h=items[:3];t=items[3:]
        return f'<div class="tabs"><button class="on" data-t="0">Популярное</button><button data-t="1">Ещё</button></div>'+''.join(f'<div class="tp {"on" if k==0 else ""}" data-p="{k}">'+''.join(f'<div class="tcard"><h3>{E(a)}</h3><b>{p}</b></div>' for a,p in g)+'</div>' for k,g in enumerate([h,t]))+note

CSS_BASE=open('base.css').read(); JS=open('base.js').read()
os.makedirs('_shots',exist_ok=True)
idx=[]
for i,r in enumerate(rows):
    c=C[i];m=M[i];slug=c[0];d={}
    pr,niche,name,typ,addr,area,rat,cnt,link,phone=r[:10]
    os.makedirs(slug,exist_ok=True)
    src=f'_raw/{i:02d}/main.jpg'
    if os.path.exists(src):
        im=Image.open(src).convert('RGB');im.thumbnail((1400,1400));im.save(f'{slug}/photo.jpg',quality=82)
    if not os.path.exists(src) and os.path.exists(f'_raw/{i:02d}/logo.jpg'): Image.open(f'_raw/{i:02d}/logo.jpg').convert('RGB').save(f'{slug}/photo.jpg',quality=88)
    lg=[f for f in (f'_raw/{i:02d}/logo.jpg',) if os.path.exists(f)]
    if lg: im=Image.open(lg[0]).convert('RGB');im.thumbnail((400,400));im.save(f'{slug}/logo.jpg',quality=88)
    d['logoimg']='<img src="logo.jpg" alt="логотип">' if lg else ''
    d.update(name=name,phone=phone,tel='+'+re.sub(r'\D','',phone),k=kind(typ,name),no=f'{i+1:02d}')
    if isinstance(rat,(int,float)): d['r']=rat;d['rtxt']=f'{float(rat):.1f}';d['rsub']=f'{cnt} оценок в 2ГИС'
    else: d['r']=0;d['rtxt']='NEW';d['rsub']='новое место в 2ГИС'
    items=SV[d['k']]; title=SEC.get(d['k'],'Услуги и цены')
    socials=''.join(f'<a href="{E(u if "link.2gis" not in u else u.split("?",1)[1])}" target="_blank" rel="noopener">{ {"vkontakte":"VK","telegram":"Telegram","whatsapp":"WhatsApp","website":"Сайт/запись","youtube":"YouTube"}[t]}</a>' for t,u in m['soc'][:4])
    bg,fg,ac,ac2,fd,fb=c[1:7]
    fonts='&'.join('family='+f.replace(' ','+')+':wght@400;600;700;800' if f not in('Bebas Neue','Russo One','Abril Fatface','Lobster','Marcellus') else 'family='+f.replace(' ','+') for f in dict.fromkeys([fd,fb]))
    dark=int(bg[1:3],16)+int(bg[3:5],16)+int(bg[5:7],16)<380
    mq=' · '.join([title.upper(),name.upper(),d['rtxt']+' В 2ГИС',addr.split(',',1)[1].strip().upper()])
    logo_nav=f'<img src="logo.jpg" class="lg" alt="">' if lg else ''
    q=addr.replace(' ','+')
    page=f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(name)} — {E(typ)} в Красногорске</title><meta name="description" content="{E(c[10])}"><meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?{fonts}&display=swap&subset=cyrillic" rel="stylesheet">
<style>:root{{--bg:{bg};--fg:{fg};--ac:{ac};--ac2:{ac2};--fd:'{fd}',serif;--fb:'{fb}',system-ui,sans-serif;--card:{'rgba(255,255,255,.06)' if dark else 'rgba(255,255,255,.75)'};--line:{'rgba(255,255,255,.14)' if dark else 'rgba(0,0,0,.1)'}}}
{CSS_BASE}</style></head><body class="v-{c[7]} s-{c[8]} k-{d['k'][:4]} {'dark' if dark else 'light'}">
<div class="intro"><span>{E(name)}</span></div><div class="demo">Демо-концепт сайта · не опубликован</div>
<nav class="nav"><a href="#" class="brand">{logo_nav}<span>{E(name)}</span></a><div class="links"><a href="#svc">{title}</a><a href="#about">О нас</a><a href="#map">Контакты</a></div><a class="btn sm" href="tel:{d['tel']}">Позвонить</a></nav>
{hero(c[7],c,d)}
<div class="marquee"><div class="mq-in"><span>{E(mq)} · </span><span>{E(mq)} · </span><span>{E(mq)} · </span><span>{E(mq)} · </span></div></div>
<section id="svc" class="wrap sec"><h2 class="rv">{title}</h2>{services(c[8],items,title)}</section>
<section id="about" class="wrap sec about"><div class="ab-img rv" data-par="0.05" style="background-image:url(photo.jpg)"></div><div><h2 class="rv">Почему к нам</h2><div class="stats"><div class="rv"><b data-count="{d['r']}">{d['rtxt']}</b><span>рейтинг 2ГИС</span></div><div class="rv"><b data-count="{cnt or 0}" data-int>{cnt or 0}</b><span>оценок гостей</span></div><div class="rv"><b>{'5' if 'пойма' in area else '10'}</b><span>минут пешком из ЖК поймы*</span></div></div><p class="rv">Мы находимся по адресу <b>{E(addr)}</b>. Подробный рассказ о команде, опыте и фото добавим вместе с вами — здесь пока демо-текст.</p><p class="note">*ориентир-заглушка, уточним.</p></div></section>
<section id="book" class="sec bookwrap"><div class="wrap book"><div><h2 class="rv">Запишитесь онлайн</h2><p class="rv">Оставьте номер — перезвоним и подберём время. Или звоните сразу: <a href="tel:{d['tel']}">{E(phone)}</a></p><div class="soc">{socials}</div></div><form onsubmit="event.preventDefault();this.classList.add('sent')" class="rv"><input placeholder="Ваше имя" required><input type="tel" placeholder="+7 (___) ___-__-__" required><select><option>{items[0][0]}</option><option>{items[1][0]}</option><option>{items[2][0]}</option></select><button class="btn">Отправить заявку</button><p class="ok">Спасибо! Это демо-форма — заявка не отправляется.</p></form></div></section>
<section id="map" class="wrap sec"><h2 class="rv">Как нас найти</h2><div class="mapbox rv"><iframe loading="lazy" src="https://yandex.ru/map-widget/v1/?text={q}&z=17" title="Карта"></iframe><div class="addr"><b>{E(addr)}</b><span>{E(area)}</span><a href="tel:{d['tel']}" class="btn">{E(phone)}</a><a href="{link}" target="_blank" rel="noopener" class="lnk">Карточка в 2ГИС →</a></div></div></section>
<footer class="wrap"><span>© {E(name)}, Красногорск</span><span>Фото — из карточки 2ГИС. Демо-концепт, цены и тексты — заглушки.</span></footer>
<a class="fab" href="tel:{d['tel']}" aria-label="Позвонить">✆</a>
<script>{JS}</script></body></html>'''
    open(f'{slug}/index.html','w').write(page)
    idx.append((pr,slug,name,typ,d['rtxt'],bool(lg),c[7]))
cards=''.join(f'<a class="it p{p}" href="{s}/index.html"><img src="{s}/photo.jpg" alt=""><div><small>{p} · {E(t)}</small><b>{E(n)}</b><span>★ {r}{" · логотип" if l else ""}</span></div></a>' for p,s,n,t,r,l,v in sorted(idx))
open('index.html','w').write(f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Демо-сайты · Павшинская пойма</title><link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@600&family=Manrope:wght@400;700&display=swap" rel="stylesheet"><style>body{{margin:0;background:#0d0d10;color:#eee;font-family:Manrope,sans-serif;padding:40px 5vw}}h1{{font-family:Unbounded;font-size:clamp(28px,5vw,56px)}}.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:18px}}.it{{color:inherit;text-decoration:none;background:#18181d;border-radius:18px;overflow:hidden;transition:.3s}}.it:hover{{transform:translateY(-6px)}}.it img{{width:100%;height:180px;object-fit:cover}}.it div{{padding:14px;display:grid;gap:4px}}small{{opacity:.6}}.pA small{{color:#7CFFB2}}</style></head><body><h1>28 демо-сайтов · Павшинская пойма</h1><p>Приоритет A → B → C. Не опубликовано.</p><div class="g">{cards}</div></body></html>''')
json.dump(idx,open('_raw/idx.json','w'),ensure_ascii=False)

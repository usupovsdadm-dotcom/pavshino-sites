import json,re,urllib.parse,html,os
from kit import D
from craft import VT
from kit import hours_rows
ix=json.load(open('_raw/idx.json'));ST=json.load(open('_raw/stories.json'))
A={ # slug: acc, ink, on, sym, galT, cta
'm-express':('#e5322d','#0d1426','#fff','🔧','В боксе','Записаться'),'autopoyma':('#ffcc00','#151515','#111','⚙','Магазин','Подобрать'),
'gorilla':('#ff5a1f','#111','#fff','🦍','Барбершоп','Записаться'),'barberclub':('#c8a165','#141210','#141210','✂','Клуб','Записаться'),
'zayushka':('#ff8a3d','#2b2350','#fff','🐰','Наши занятия','Записаться'),'mary-poppins':('#b23a48','#1f2a44','#fff','☂','Школа','Записаться'),
'pochemuchka':('#3d7bff','#16224a','#fff','?','Студия','Записаться'),'hvost':('#c56a3d','#2a1d17','#fff','☕','Кофейня','Заказать'),
'belyi-krolik':('#e94e77','#1a1426','#fff','🐇','Логово','Заказать'),'coffee-flat':('#8a5a3b','#221812','#fff','☕','Квартира','Заказать'),
'crush':('#d9468f','#1c1018','#fff','♥','Студия','Записаться'),'organika':('#6a8f4e','#1e2a18','#fff','🌿','Студия','Записаться'),
'beauty-time':('#c08a5b','#1f1712','#fff','✦','Студия','Записаться'),'pink-code':('#ff4fa3','#2a0f22','#fff','💅','Студия','Записаться'),
'london':('#c8102e','#0f1b33','#fff','☂','Барбершоп','Записаться'),'sosedi':('#e8a33d','#17130f','#17130f','💡','Соседи','Записаться'),
'stefanny':('#9c3b2a','#2b2118','#fff','🧵','Ателье','Записаться'),'mia':('#1aa6b7','#0e2a33','#fff','🫧','Химчистка','Заявка'),
'vsegda-kofe':('#ff6a2b','#1c140f','#fff','☕','Кофейня','Заказать'),'495':('#2e4bff','#111','#fff','4','Кофейня','Заказать'),
'prana':('#5b7a4a','#24301f','#fff','🍃','Кофейня','Написать'),'negrul':('#e3a72f','#3a0f0c','#3a0f0c','🥟','Кафе','Заказать'),
'popnails':('#ff2e88','#111','#fff','💥','Студия','Записаться'),'mindal':('#c98b7b','#4a2e2a','#fff','🌸','Студия','Записаться'),
'territoriya-manikyura':('#3fd0a6','#0f2a2a','#0f2a2a','✚','Студия','Записаться'),'yourmed':('#0a7cff','#0b2545','#fff','❤','Клиника','Записаться'),
'gruzinskie-kanikuly':('#b3262d','#1b120d','#fff','🍷','Ресторан','Бронь'),'lak-mi':('#ff3df2','#120a1f','#120a1f','💅','Студия','Записаться')}
E=html.escape
for i,r in enumerate(ix):
    slug=r[1];o=D[i];p=f'{slug}/index.html';s=open(p).read()
    s=re.sub(r'<!--MOB-->.*?<!--/MOB-->','',s,flags=re.S)
    acc,ink,on,sym,galT,cta=A[slug]
    photos=['photo.jpg']+ST.get(slug,[])
    rt=o['rating'];rt=f"{float(rt):.1f}".replace('.',',') if isinstance(rt,(int,float)) else None
    sl=[]
    if rt and o['cnt']:sl.append({'h':f"<b>{rt}★</b><small>{o['cnt']} оценок в 2ГИС</small>"})
    if o['reviews']:
        rv=o['reviews'][0];t=rv['t'][:170]+('…' if len(rv['t'])>170 else '')
        sl.append({'h':f"<q>«{E(t)}»</q><small>— {E(rv['n'])}, отзыв в 2ГИС</small>",'bg':ink,'fg':'#fff'})
    hr=hours_rows(o['hours'])
    if hr:sl.append({'h':'<q>'+'<br>'.join(f'{a} · {b}' for a,b in hr)+f"</q><small>{E(o['addr'].replace('Красногорск, ',''))}</small>",'bg':'#fff','fg':'#111'})
    if o['prices']:
        a,b=o['prices'][0];sl.append({'h':f"<small>{E(a)}</small><b style='font-size:min(12vw,80px)'>{E(b)}</b>"})
    cfg=dict(name=o['name'],type=o['type'],addr=o['addr'].replace('Красногорск, ',''),tel=o['tel'],phone=o['phone'],wa=o['soc'].get('wa'),gis=o['gis'],
      route='https://yandex.ru/maps/?text='+urllib.parse.quote(o['addr']),acc=acc,ink=ink,on=on,sym=sym,galT=galT,cta=cta,photos=photos,slides=sl,
      fx=[acc,'#ffffff',ink])
    inj='<!--MOB--><link rel="stylesheet" href="../kit/mob.css"><script>window.MOB='+json.dumps(cfg,ensure_ascii=False).replace('</','<\\/')+'</script><script src="../kit/mob.js" defer></script>'
    if 'startViewTransition' not in s: inj+=VT
    inj+='<!--/MOB-->'
    s=s.replace('</body>',inj+'</body>',1) if '</body>' in s else s+inj
    open(p,'w').write(s)
print('ok')

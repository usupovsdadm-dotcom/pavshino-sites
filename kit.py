import json,re,html
D={o['i']:o for o in json.load(open('_raw/data.json'))}
E=html.escape
def hours_rows(h):
    days=['Пн','Вт','Ср','Чт','Пт','Сб','Вс'];out=[]
    for d in days: out.append((d,h.get(d,'выходной')))
    # compress
    g=[];
    for d,v in out:
        if g and g[-1][2]==v: g[-1][1]=d
        else: g.append([d,d,v])
    return [((a if a==b else f'{a}–{b}'),v) for a,b,v in g]
def wa_js(o):
    wa=o['soc'].get('wa')
    return f"""<script>function waSend(e,f){{e.preventDefault();var L=[].slice.call(f.querySelectorAll('input,select,textarea')).filter(function(x){{return x.value}}).map(function(x){{return (x.getAttribute('aria-label')||x.placeholder||'').replace(/[:*]/g,'')+': '+x.value}});var t='Здравствуйте! Пишу с сайта {E(o['name'])}. Хочу записаться.\\n'+L.join('\\n');{f"window.open('https://wa.me/{wa}?text='+encodeURIComponent(t),'_blank');" if wa else f"location.href='tel:{o['tel']}';"}return false}}</script>"""
def socials(o,cls=''):
    L=[]
    s=o['soc']
    if s.get('wa'):L.append(('WhatsApp',f"https://wa.me/{s['wa']}"))
    for u in s.get('telegram',[]):L.append(('Telegram',u))
    for u in s.get('vkontakte',[]):L.append(('ВКонтакте',u))
    for u in s.get('youtube',[]):L.append(('YouTube',u))
    for u in s.get('web',[]):
        n='Онлайн-запись' if any(k in u for k in ['yclients','dikidi','sonline']) else ('Taplink' if 'taplink' in u else ('MAX' if 'max.ru' in u else 'Сайт'))
        if 't.me/' in u:n='Telegram-канал'
        if 'clck.ru' in u:n='Онлайн-запись'
        L.append((n,u))
    L.append(('2ГИС',o['gis']))
    seen=set();R=[]
    for n,u in L:
        if u in seen:continue
        seen.add(u);R.append(f'<a class="{cls}" href="{E(u)}" target="_blank" rel="noopener">{n}</a>')
    return ''.join(R)
def form_attr(): return 'onsubmit="return waSend(event,this)"'
def btn_label(o): return 'Написать в WhatsApp' if o['soc'].get('wa') else 'Позвонить'

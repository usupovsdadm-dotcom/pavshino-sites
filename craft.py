from common import *
def tail(o,svc_opts,lead='Запись',sub=''):
    R=rating(o)
    rv=revs(o,'<figure class="q rv"><blockquote>«{t}»</blockquote><figcaption>— {n}, отзыв в 2ГИС</figcaption></figure>')
    rvs=f'''<section class="s-rv" id="reviews"><p class="cap rv">Отзывы · 2ГИС</p><h2 class="rv">{R or ''}{' <small>★ · '+str(o['cnt'])+' оценок</small>' if R else 'Отзывы'}</h2><div class="qs">{rv}</div></section>''' if o['reviews'] else ''
    opts=''.join(f'<option>{E(s)}</option>' for s in svc_opts)
    return rvs+f'''<section class="s-vis" id="visit"><div class="vi"><p class="cap rv">{E(o['addr'])}</p><h2 class="rv">{lead}</h2>{('<p class="rv">'+sub+'</p>') if sub else ''}<ul class="hr rv">{hrs(o,'<li><span>{d}</span><b>{h}</b></li>')}</ul>
<form class="rv" {form_attr()}><input aria-label="Имя" placeholder="Ваше имя" required><input aria-label="Телефон" type="tel" placeholder="Телефон" required><select aria-label="Услуга">{opts}</select><button class="btn" data-mag>{btn_label(o)}</button></form>
<div class="so rv">{socials(o)}<a href="tel:{o['tel']}">{E(o['phone'])}</a></div></div><div class="mp">{map_iframe(o)}</div></section>
<footer><span>© {E(o['name'])} · {E(o['addr'])}</span><a href="{o['gis']}" target="_blank" rel="noopener">Карточка в 2ГИС</a></footer>'''
VT='''<style>@view-transition{navigation:auto}</style><script>document.addEventListener('click',function(e){var a=e.target.closest('a[href^="#"]');if(!a)return;var t=document.querySelector(a.getAttribute('href'));if(!t)return;e.preventDefault();var go=function(){t.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'})};document.startViewTransition&&!matchMedia('(prefers-reduced-motion: reduce)').matches?document.startViewTransition(go):go()})</script>'''
def page(o,slug,title,fonts,css,body):
    write(slug,head(o,title,fonts,css)+body+JS_BASE+wa_js(o)+VT+'</body></html>')

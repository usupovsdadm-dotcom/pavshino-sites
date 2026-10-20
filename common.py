from kit import *
import urllib.parse,os
def head(o,title,fonts,css):
    return f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex,nofollow"><script>document.documentElement.classList.add("js")</script>
<title>{E(title)}</title><meta name="description" content="{E(o['name'])} — {E(o['type'])}, {E(o['addr'])}. Телефон {E(o['phone'])}.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">
<style>*{{box-sizing:border-box;margin:0}}html{{overflow-x:clip;-webkit-text-size-adjust:100%}}body{{overflow-x:clip}}img{{max-width:100%;display:block}}a{{color:inherit}}
.js .rv{{opacity:0;transform:translateY(36px);transition:opacity 1s cubic-bezier(.2,.8,.2,1),transform 1s cubic-bezier(.2,.8,.2,1)}}.rv.on{{opacity:1!important;transform:none!important}}
@media(prefers-reduced-motion:reduce){{*,*::before,*::after{{animation:none!important;transition:none!important;scroll-behavior:auto!important}}.js .rv{{opacity:1;transform:none}}}}
{css}</style></head><body>'''
def map_iframe(o,style=''):
    q=urllib.parse.quote(o['addr'])
    return f'<iframe loading="lazy" src="https://yandex.ru/map-widget/v1/?text={q}&z=17" title="Карта: {E(o["addr"])}" style="{style}"></iframe>'
def revs(o,tpl):
    return ''.join(tpl.format(n=E(r['n']),t=E(r['t'][:280]+('…' if len(r['t'])>280 else ''))) for r in o['reviews'])
def hrs(o,tpl):
    return ''.join(tpl.format(d=a,h=v) for a,v in hours_rows(o['hours']))
def rating(o):
    return (f"{float(o['rating']):.1f}".replace('.',',') if isinstance(o['rating'],(int,float)) else None)
JS_BASE='''<script>(function(){var R=matchMedia('(prefers-reduced-motion: reduce)').matches||/shot/.test(location.search);var io='IntersectionObserver' in window?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}})},{threshold:.12,rootMargin:'0px 0px -5% 0px'}):null;document.querySelectorAll('.rv').forEach(function(el,i){el.style.transitionDelay=(i%4)*.08+'s';io&&!R?io.observe(el):el.classList.add('on')});setTimeout(function(){document.querySelectorAll('.rv').forEach(function(el){var r=el.getBoundingClientRect();if(r.top<innerHeight)el.classList.add('on')})},2500);
if(!R&&matchMedia('(hover:hover) and (pointer:fine)').matches){document.querySelectorAll('[data-mag]').forEach(function(b){b.addEventListener('mousemove',function(e){var r=b.getBoundingClientRect();b.style.transform='translate('+((e.clientX-r.left-r.width/2)*.3)+'px,'+((e.clientY-r.top-r.height/2)*.4)+'px)'});b.addEventListener('mouseleave',function(){b.style.transform=''})})}})();</script>'''
def write(slug,html):
    os.makedirs(slug,exist_ok=True);open(f'{slug}/index.html','w').write(html);print('wrote',slug,len(html))

from common import *
o=D[14];R=rating(o)
css='''
:root{--nv:#0f1b33;--rd:#c8102e;--cr:#f3ede2;--gd:#c9a35b;--ink:#0b0f18}
body{background:var(--cr);color:var(--ink);font:400 17px/1.6 'Inter Tight',sans-serif}
.cap{font:600 11px 'Inter Tight';letter-spacing:.32em;text-transform:uppercase}
nav{position:fixed;top:0;left:0;right:0;z-index:40;display:flex;justify-content:space-between;align-items:center;padding:16px 4vw;color:#fff;background:#0f1b33cc;backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
nav b{font:400 26px 'Abril Fatface'}
.btn{display:inline-flex;align-items:center;gap:12px;background:var(--rd);color:#fff;padding:17px 30px;border-radius:999px;font:600 15px 'Inter Tight';text-decoration:none;border:0;cursor:pointer;transition:transform .3s,background .3s}.btn:hover{background:var(--nv)}.btn.o{background:transparent;border:1.5px solid currentColor}
.hero{background:var(--nv);color:var(--cr);min-height:100svh;display:grid;grid-template-rows:1fr auto;overflow:hidden;position:relative}
.hero .ph{position:absolute;right:0;top:0;width:46%;height:100%;object-fit:cover;filter:grayscale(.2) contrast(1.05)}
.hero .ph{clip-path:inset(0 0 0 0 round 0 0 0 220px)}
.kin{position:relative;z-index:2;padding:22vh 4vw 0;font:400 clamp(84px,17vw,280px)/.82 'Abril Fatface';letter-spacing:-.02em}
.kin span{display:inline-block}
.js .kin span{transform:translateY(110%) rotate(8deg);opacity:0;transition:transform 1.1s cubic-bezier(.2,.9,.2,1),opacity 1.1s}
.go .kin span{transform:none;opacity:1}
.kin .r{color:var(--rd)}
.sub{position:relative;z-index:2;padding:4vh 4vw 6vh;display:flex;gap:30px;align-items:end;justify-content:space-between;flex-wrap:wrap}
.sub p{max-width:30ch;font-size:clamp(18px,1.7vw,22px)}
.rt{display:flex;gap:14px;align-items:center}.rt b{font:400 64px/1 'Abril Fatface';color:var(--gd)}
.tube{padding:clamp(80px,12vw,150px) 4vw;position:relative}
.tube h2,.vis h2,.rvw h2{font:400 clamp(44px,6.5vw,100px)/.95 'Abril Fatface';letter-spacing:-.01em}
.line{position:relative;margin-top:60px;padding-left:70px}
.line::before{content:"";position:absolute;left:24px;top:10px;bottom:10px;width:12px;border-radius:8px;background:var(--rd)}
.line .tr{position:absolute;left:24px;top:10px;width:12px;border-radius:8px;background:var(--nv);height:var(--p,0%)}
.st{position:relative;padding:22px 0;display:flex;justify-content:space-between;align-items:baseline;gap:20px;border-bottom:1px dashed #0f1b3333}
.st::before{content:"";position:absolute;left:-58px;top:28px;width:24px;height:24px;border-radius:50%;background:#fff;border:6px solid var(--nv);transition:background .4s}
.st.on::before{background:var(--rd)}
.st h3{font:600 clamp(22px,2.6vw,34px)/1.1 'Inter Tight'}.st b{font-weight:600;white-space:nowrap}.st small{display:block;font-size:13px;opacity:.6;font-weight:400}
.rvw{background:var(--rd);color:#fff;padding:clamp(80px,12vw,150px) 4vw}
.qs{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:50px}
.q{margin:0;border-top:2px solid #fff;padding-top:24px}.q blockquote{font:400 italic 22px/1.35 'Abril Fatface';margin-bottom:16px}.q figcaption{font-size:13px;opacity:.8}
.vis{display:grid;grid-template-columns:1fr 1fr;background:var(--nv);color:var(--cr)}
.vis>div{padding:clamp(60px,9vw,120px) 4vw}
.hr{list-style:none;padding:0;margin:26px 0}.hr li{display:flex;justify-content:space-between;padding:14px 0;border-bottom:1px solid #ffffff22;font-size:18px}
form{display:grid;gap:12px;margin-top:26px}input,select{font:16px 'Inter Tight';padding:17px 20px;border-radius:14px;border:1px solid #ffffff33;background:#ffffff0d;color:#fff}select option{color:#000}
.so{display:flex;flex-wrap:wrap;gap:10px;margin-top:20px}.so a{padding:11px 18px;border-radius:999px;border:1px solid #ffffff44;text-decoration:none;font-size:14px;transition:.3s}.so a:hover{background:var(--rd);border-color:var(--rd)}
.vis iframe{width:100%;height:100%;min-height:480px;border:0;display:block;filter:grayscale(.3)}
footer{background:var(--ink);color:#9aa3b5;padding:26px 4vw;display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;font-size:13px}
@supports (animation-timeline: scroll()){.hero .ph{animation:zoom linear both;animation-timeline:scroll();animation-range:0 100vh}@keyframes zoom{to{transform:scale(1.15);filter:grayscale(1)}}}
@media(max-width:860px){.hero .ph{position:relative;width:100%;height:46vh;clip-path:inset(0 0 0 0 round 0 0 0 120px);order:-1}.hero{display:flex;flex-direction:column}.kin{padding-top:4vh}.qs,.vis{grid-template-columns:1fr}.vis iframe{min-height:340px}.line{padding-left:56px}.line::before,.line .tr{left:14px}.st::before{left:-50px}}
'''
pr=[('Мужская стрижка','от 1 800 ₽','по данным 2ГИС'),('Оформление бороды','по записи',''),('Стрижка + борода','по записи',''),('Детская стрижка','по записи','')]
st=''.join(f'<div class="st"><div><h3>{a}</h3><small>{c}</small></div><b>{b}</b></div>' for a,b,c in pr)
html=head(o,'London — барбершоп на Молодёжной, 4 · Красногорск','family=Abril+Fatface&family=Inter+Tight:wght@400;600',css)+f'''
<nav><b>London</b><a class="btn" data-mag href="#visit">Записаться</a></nav>
<header class="hero" id="hero"><img class="ph" src="photo.jpg" alt="Работа барбера London"><div class="kin" aria-label="London"><span>L</span><span>o</span><span>n</span><span>d</span><span>o</span><span class="r">n</span></div>
<div class="sub"><div><p class="cap" style="margin-bottom:14px">барбершоп · Молодёжная ул., 4, 2 этаж</p><p>Британская строгость, русская душевность. Стрижки и борода — ежедневно с 10 до 22.</p><div style="margin-top:24px;display:flex;gap:12px;flex-wrap:wrap"><a class="btn" data-mag href="#visit">Записаться</a><a class="btn o" data-mag href="tel:{o['tel']}">{E(o['phone'])}</a></div></div>
<div class="rt"><b>{R}</b><span class="cap">★ 2ГИС<br>{o['cnt']} оценок</span></div></div></header>
<section class="tube"><p class="cap rv">The Barber Line</p><h2 class="rv">Маршрут<br>по услугам</h2><div class="line" id="line"><div class="tr"></div>{st}</div><p style="margin-top:24px;opacity:.6">Стоимость остальных услуг — при записи.</p></section>
<section class="rvw"><p class="cap">отзывы гостей · 2ГИС</p><h2 class="rv">«Отличный барбер»</h2><div class="qs">{revs(o,'<figure class="q rv"><blockquote>«{t}»</blockquote><figcaption>{n}</figcaption></figure>')}</div></section>
<section class="vis" id="visit"><div><p class="cap">Mind the time</p><h2 class="rv">Запись</h2><p style="margin-top:16px">{E(o['addr'])}</p><ul class="hr">{hrs(o,'<li><span>{d}</span><b>{h}</b></li>')}</ul>
<form {form_attr()}><input aria-label="Имя" placeholder="Имя" required><input aria-label="Телефон" type="tel" placeholder="Телефон" required><select aria-label="Услуга"><option>Мужская стрижка</option><option>Борода</option><option>Стрижка + борода</option></select><button class="btn" data-mag>{btn_label(o)}</button></form><div class="so">{socials(o)}</div></div>{map_iframe(o)}</section>
<footer><span>© London barbershop</span><span>Стоимость услуг уточняйте при записи</span></footer>
<script>(function(){{var h=document.getElementById('hero');h.querySelectorAll('.kin span').forEach(function(s,i){{s.style.transitionDelay=(.15+i*.08)+'s'}});requestAnimationFrame(function(){{setTimeout(function(){{h.classList.add('go')}},60)}});
var ln=document.getElementById('line'),ss=[].slice.call(ln.querySelectorAll('.st'));function f(){{var r=ln.getBoundingClientRect(),p=Math.min(1,Math.max(0,(innerHeight*.65-r.top)/r.height));ln.style.setProperty('--p',p*100+'%');ss.forEach(function(s){{s.classList.toggle('on',s.offsetTop<p*ln.offsetHeight)}})}}addEventListener('scroll',function(){{requestAnimationFrame(f)}},{{passive:true}});f()}})();</script>
{JS_BASE}{wa_js(o)}</body></html>'''
write('london',html)

from craft import *
import sys
def TC(bg,fg,acc,hf,card='transparent',btxt='#fff',r='999px'):
    return f'''.cap{{font-size:12px;letter-spacing:.24em;text-transform:uppercase;font-weight:600;opacity:.75}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:10px;background:{acc};color:{btxt};padding:17px 30px;border-radius:{r};font-weight:700;font-size:15px;text-decoration:none;border:0;cursor:pointer;transition:transform .35s cubic-bezier(.2,.8,.2,1),box-shadow .35s;font-family:inherit}}.btn:hover{{box-shadow:0 14px 34px -10px {acc}}}
.btn.o{{background:transparent;color:inherit;border:1.5px solid currentColor}}
.s-rv,.s-vis{{padding:clamp(70px,11vw,140px) 5vw}}.s-rv h2,.s-vis h2,.h2{{font-family:{hf};font-size:clamp(40px,6vw,92px);line-height:.98;margin:14px 0 10px}}.s-rv h2 small{{font-size:.32em;opacity:.7;font-family:inherit;vertical-align:middle}}
.qs{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:22px;margin-top:40px}}.q{{margin:0;background:{card};padding:28px;border-radius:22px;border:1px solid {fg}22}}.q blockquote{{font-size:17px;line-height:1.55;margin-bottom:14px}}.q figcaption{{font-size:13px;opacity:.65}}
.s-vis{{display:grid;grid-template-columns:1.05fr 1fr;gap:5vw;align-items:start;background:{bg};color:{fg}}}
.hr{{list-style:none;padding:0;margin:24px 0}}.hr li{{display:flex;justify-content:space-between;gap:12px;padding:13px 0;border-bottom:1px solid {fg}22}}
form{{display:grid;gap:11px;margin-top:22px}}input,select{{font:inherit;font-size:16px;padding:16px 18px;border-radius:14px;border:1px solid {fg}33;background:{fg}0a;color:inherit}}select option{{color:#000}}
.so{{display:flex;flex-wrap:wrap;gap:9px;margin-top:22px}}.so a{{padding:10px 17px;border-radius:999px;border:1px solid {fg}44;text-decoration:none;font-size:14px;transition:.3s}}.so a:hover{{background:{acc};color:{btxt};border-color:{acc}}}
.mp{{border-radius:26px;overflow:hidden;position:sticky;top:90px}}.mp iframe{{width:100%;height:560px;border:0;display:block}}
footer{{padding:26px 5vw;display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;font-size:13px;opacity:.75;background:{bg};color:{fg};border-top:1px solid {fg}1a}}
nav{{position:fixed;inset:0 0 auto 0;z-index:50;display:flex;justify-content:space-between;align-items:center;padding:14px 5vw}}nav .btn{{padding:12px 22px}}
.svc{{list-style:none;padding:0}}.hero>*,.s-vis>*{{min-width:0}}select{{width:100%;max-width:100%}}
@media(max-width:860px){{.s-vis{{grid-template-columns:1fr}}.mp{{position:static}}.mp iframe{{height:360px}}}}'''
def LI(rows,tpl='<li class="rv"><span>{a}</span><b>{b}</b></li>'): return ''.join(tpl.format(a=E(a),b=E(b)) for a,b in rows)
S={}
def site(f): S[f.__name__]=f;return f

@site
def sosedi():
    o=D[15]
    css=TC('#17130f','#f4ead9','#e8a33d',"'Unbounded'",'#ffffff08','#17130f')+'''
body{background:#17130f;color:#f4ead9;font:400 17px/1.6 'Golos Text',sans-serif}
nav{background:#17130fcc;backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}nav b{font:700 20px 'Unbounded'}
.hero{min-height:100svh;padding:120px 5vw 60px;display:grid;grid-template-columns:1.1fr 1fr;gap:5vw;align-items:center}
.hero h1{font:800 clamp(56px,9vw,150px)/.9 'Unbounded';letter-spacing:-.03em}.hero h1 i{font-style:normal;color:#e8a33d}
.hero p{max-width:34ch;margin:26px 0 30px;font-size:19px;opacity:.85}
.fac{background:#2a221b;border-radius:16px 16px 0 0;padding:26px;display:grid;grid-template-columns:repeat(4,1fr);gap:14px;position:relative;box-shadow:0 40px 80px -30px #000}
.fac::before{content:"СОСЕДИ";position:absolute;top:-34px;left:0;right:0;text-align:center;font:800 18px 'Unbounded';letter-spacing:.5em;color:#e8a33d;text-shadow:0 0 18px #e8a33d}
.w{aspect-ratio:3/4;border-radius:6px;background:#0d0a08;border:3px solid #3a3027;transition:background .6s,box-shadow .6s}
.w.l{background:linear-gradient(#ffcf7a,#e8a33d);box-shadow:0 0 30px #e8a33d88}
.door{grid-column:2/4;aspect-ratio:2/1.3;background:url(photo.jpg) center/cover;border-radius:8px 8px 0 0;border:3px solid #e8a33d}
.pr{padding:clamp(70px,11vw,140px) 5vw;background:#f4ead9;color:#17130f}
.pr .svc li{display:grid;grid-template-columns:1fr auto;gap:20px;padding:22px 0;border-bottom:1.5px solid #17130f22;font-size:clamp(18px,2vw,24px)}.pr .svc b{font-family:'Unbounded';font-weight:700}
.pr .src{margin-top:20px;font-size:14px;opacity:.6}
@media(max-width:860px){.hero{grid-template-columns:1fr;padding-top:100px}.fac{margin-top:40px}}'''
    rows=o['prices']
    body=f'''<nav><b>Соседи</b><a class="btn" data-mag href="#visit">Записаться</a></nav>
<header class="hero"><div><p class="cap">мужская парикмахерская · Молодёжная, 2</p><h1>Стрижём<br><i>по-соседски</i></h1><p>Без пафоса, но с вниманием к деталям. Каждый день с 12:00 до 22:00 — зашёл после работы и вышел другим человеком.</p><div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn" data-mag href="#visit">Выбрать время</a><a class="btn o" href="#price">Прайс</a></div></div>
<div class="fac" id="fac" aria-hidden="true">{'<div class="w"></div>'*8}<div class="w"></div><div class="door"></div><div class="w"></div></div></header>
<section class="pr" id="price"><p class="cap rv">прайс · онлайн-запись Sonline</p><h2 class="h2 rv">Услуги и цены</h2><ul class="svc">{LI(rows,'<li class="rv"><span>{a}</span><b>{b}</b></li>')}</ul><p class="src">Цены — из онлайн-записи салона; актуальность уточняйте при записи.</p></section>
{tail(o,[a for a,b in rows])}
<script>(function(){{var ws=[].slice.call(document.querySelectorAll('#fac .w'));var R=matchMedia('(prefers-reduced-motion: reduce)').matches;function f(){{var p=R?1:Math.min(1,Math.max(0,scrollY/(innerHeight*.7)+.25));ws.forEach(function(w,i){{w.classList.toggle('l',((i*7)%ws.length)/ws.length<p)}})}}addEventListener('scroll',function(){{requestAnimationFrame(f)}},{{passive:true}});f()}})()</script>'''
    page(o,'sosedi','Соседи — мужская парикмахерская, Молодёжная ул., 2','family=Unbounded:wght@700;800&family=Golos+Text:wght@400;600',css,body)

@site
def stefanny():
    o=D[16]
    css=TC('#efe6d8','#2b2118','#9c3b2a',"'Cormorant Garamond'",'#fff8','#fff')+'''
body{background:#efe6d8;color:#2b2118;font:400 17px/1.6 'Manrope',sans-serif}
nav{background:#efe6d8e6;backdrop-filter:blur(8px)}nav b{font:600 italic 26px 'Cormorant Garamond'}
.hero{min-height:100svh;display:grid;grid-template-columns:1fr 1fr;padding-top:70px}
.hero .t{padding:8vh 5vw;display:flex;flex-direction:column;justify-content:center}
.hero h1{font:500 clamp(60px,8.5vw,140px)/.9 'Cormorant Garamond';letter-spacing:-.01em}.hero h1 em{color:#9c3b2a}
.hero p{max-width:36ch;margin:24px 0 30px;font-size:18px}
.ph{position:relative;margin:4vw;border-radius:200px 200px 24px 24px;overflow:hidden}.ph img{width:100%;height:100%;object-fit:cover}
.tape{height:64px;background:#e9c46a;position:relative;overflow:hidden;border-block:2px solid #2b2118;display:flex;align-items:center}
.tape .tr{display:flex;white-space:nowrap;font:700 13px 'Manrope';will-change:transform}
.tape .tr span{display:inline-block;width:60px;border-left:2px solid #2b2118;height:64px;padding:6px 0 0 4px;position:relative}
.tape .tr span::after{content:"";position:absolute;left:28px;bottom:0;height:18px;border-left:1.5px solid #2b2118}
.sv{padding:clamp(70px,11vw,140px) 5vw}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:40px}
.cd{background:#fff;border-radius:22px;padding:32px;position:relative}
.cd svg{width:100%;height:24px;margin-bottom:22px}.cd path{stroke:#9c3b2a;stroke-width:2.5;fill:none;stroke-dasharray:8 7;stroke-dashoffset:300;transition:stroke-dashoffset 2.2s ease}.cd.on path{stroke-dashoffset:0}
.cd h3{font:600 30px/1.05 'Cormorant Garamond';margin-bottom:10px}.cd b{display:block;margin-top:16px;color:#9c3b2a}
@media(max-width:860px){.hero{grid-template-columns:1fr}.ph{height:52vh;order:-1;margin:20px 5vw 0}.cards{grid-template-columns:1fr}}'''
    cs=[('Ремонт одежды','Подгонка по фигуре, замена молний, подшив брюк и юбок.'),('Швейное ателье','Индивидуальный пошив и реставрация любимых вещей.'),('Ремонт обуви и кожгалантереи','Кожаные сумки, ремни, обувь — бережный ремонт.')]
    cards=''.join(f'<div class="cd rv"><svg viewBox="0 0 300 24" preserveAspectRatio="none"><path d="M0 12 Q 37 0 75 12 T 150 12 T 225 12 T 300 12"/></svg><h3>{a}</h3><p>{b}</p><b>Стоимость — по записи</b></div>' for a,b in cs)
    body=f'''<nav><b>Stefanny</b><a class="btn" data-mag href="#visit">Записаться</a></nav>
<header class="hero"><div class="t"><p class="cap">ателье · Красногорский б-р, 32 · ЖК Прибрежный</p><h1>Сидит<br><em>как влитое</em></h1><p>Ремонт и пошив одежды, ремонт обуви и кожаных изделий. Ежедневно с 11:00 до 20:00, 2 филиала.</p><div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn" data-mag href="#visit">Записаться на примерку</a><a class="btn o" href="tel:{o['tel']}">{E(o['phone'])}</a></div></div><div class="ph"><img src="photo.jpg" alt="Ателье Stefanny"></div></header>
<div class="tape" aria-hidden="true"><div class="tr" id="tp">{''.join(f'<span>{i}</span>' for i in range(0,150))}</div></div>
<section class="sv"><p class="cap rv">что мы делаем · по данным 2ГИС</p><h2 class="h2 rv">Три ремесла<br>под одной крышей</h2><div class="cards">{cards}</div></section>
{tail(o,[a for a,b in cs])}
<script>(function(){{var t=document.getElementById('tp');if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;addEventListener('scroll',function(){{t.style.transform='translateX('+(-scrollY*.6)+'px)'}},{{passive:true}})}})()</script>'''
    page(o,'stefanny','Stefanny — ателье, Красногорский б-р, 32','family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Manrope:wght@400;700',css,body)

@site
def mia():
    o=D[17]
    css=TC('#eef5f7','#0e2a33','#1aa6b7',"'Onest'",'#fff','#fff')+'''
body{background:#eef5f7;color:#0e2a33;font:400 17px/1.6 'Onest',sans-serif}
nav{background:#eef5f7d9;backdrop-filter:blur(8px)}nav b{font:800 24px 'Onest';color:#1aa6b7}
.hero{min-height:100svh;padding:110px 5vw 50px;display:grid;grid-template-columns:1fr 1fr;gap:5vw;align-items:center}
.hero h1{font:800 clamp(52px,8vw,128px)/.92 'Onest';letter-spacing:-.04em}.hero h1 span{color:#1aa6b7}
.hero p{margin:22px 0 30px;max-width:34ch;font-size:18px}
.wipe{position:relative;aspect-ratio:4/5;border-radius:30px;overflow:hidden;touch-action:pan-y;box-shadow:0 40px 80px -40px #0e2a3388}
.wipe img{width:100%;height:100%;object-fit:cover}.wipe canvas{position:absolute;inset:0;width:100%;height:100%;cursor:crosshair}
.wipe .hint{position:absolute;left:50%;bottom:22px;transform:translateX(-50%);background:#fff;padding:10px 18px;border-radius:999px;font-size:14px;font-weight:600;pointer-events:none;transition:opacity .5s}
.st{padding:clamp(70px,11vw,140px) 5vw;background:#0e2a33;color:#eef5f7}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:40px;counter-reset:s}
.sp{border:1px solid #ffffff22;border-radius:24px;padding:30px;counter-increment:s}.sp::before{content:"0" counter(s);font:800 54px 'Onest';color:#1aa6b7;display:block;margin-bottom:12px}
.sp h3{font-size:24px;margin-bottom:8px}
.bub{position:absolute;border-radius:50%;background:radial-gradient(circle at 30% 30%,#fff,#bfe9ef 40%,#1aa6b722 70%);animation:fl 9s ease-in-out infinite;pointer-events:none}
@keyframes fl{50%{transform:translateY(-30px)}}
@media(max-width:860px){.hero{grid-template-columns:1fr}.steps{grid-template-columns:1fr}}'''
    body=f'''<nav><b>Mia</b><a class="btn" data-mag href="#visit">Позвонить</a></nav>
<header class="hero"><div><p class="cap">химчистка · Подмосковный б-р, 2</p><h1>Ковёр<br>как <span>новый</span></h1><p>Чистка ковров, химчистка одежды и текстиля. Пн–Сб 11:00–19:00, Вс 11:00–18:00. Проведите по фото — и увидите разницу.</p><div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn" data-mag href="#visit">Оставить заявку</a><a class="btn o" href="tel:{o['tel']}">{E(o['phone'])}</a></div></div>
<div class="wipe" id="wp"><img src="photo.jpg" alt="Химчистка Mia"><canvas id="cv" aria-hidden="true"></canvas><span class="hint" id="ht">Проведите, чтобы очистить ✦</span></div></header>
<section class="st"><p class="cap rv">услуги · по данным 2ГИС</p><h2 class="h2 rv">Что мы чистим</h2><div class="steps"><div class="sp rv"><h3>Чистка ковров</h3><p>Ковры и ковровые покрытия.</p></div><div class="sp rv"><h3>Химчистка одежды</h3><p>Повседневная и деликатная одежда.</p></div><div class="sp rv"><h3>Текстиль</h3><p>Домашний текстиль.</p></div></div><p style="margin-top:24px;opacity:.6">Стоимость — по запросу, рассчитывается по изделию.</p></section>
{tail(o,['Чистка ковра','Химчистка одежды','Текстиль'],'Заявка')}
<script>(function(){{var c=document.getElementById('cv'),w=document.getElementById('wp'),h=document.getElementById('ht'),x=c.getContext('2d');if(matchMedia('(prefers-reduced-motion: reduce)').matches){{c.remove();h.remove();return}}
function sz(){{var r=w.getBoundingClientRect(),d=Math.min(2,devicePixelRatio||1);c.width=r.width*d;c.height=r.height*d;x.setTransform(d,0,0,d,0,0);var g=x.createLinearGradient(0,0,r.width,r.height);g.addColorStop(0,'rgba(120,100,70,.82)');g.addColorStop(1,'rgba(80,70,55,.88)');x.globalCompositeOperation='source-over';x.fillStyle=g;x.fillRect(0,0,r.width,r.height);for(var i=0;i<900;i++){{x.fillStyle='rgba(40,30,20,'+Math.random()*.25+')';x.fillRect(Math.random()*r.width,Math.random()*r.height,2,2)}}x.globalCompositeOperation='destination-out'}}sz();
function pt(e){{var r=c.getBoundingClientRect(),p=e.touches?e.touches[0]:e;x.beginPath();x.arc(p.clientX-r.left,p.clientY-r.top,46,0,7);x.fill();h.style.opacity=0}}
c.addEventListener('pointermove',pt);c.addEventListener('touchmove',pt,{{passive:true}});
var t=0,auto=setInterval(function(){{t+=.09;var r=c.getBoundingClientRect();x.beginPath();x.arc(r.width*(.5+.38*Math.sin(t)),r.height*(.2+t*.03),40,0,7);x.fill();if(t>22)clearInterval(auto)}},40)}})()</script>'''
    page(o,'mia','Mia — химчистка и чистка ковров, Подмосковный б-р, 2','family=Onest:wght@400;600;800',css,body)

@site
def vsegda_kofe():
    o=D[18]
    css=TC('#1c140f','#f6efe4','#ff6a2b',"'Oswald'",'#ffffff08','#fff')+'''
body{background:#1c140f;color:#f6efe4;font:400 17px/1.6 'IBM Plex Sans',sans-serif}
nav{background:#1c140fcc;backdrop-filter:blur(10px)}nav b{font:400 30px 'Oswald';letter-spacing:.04em}nav img{height:36px;border-radius:8px}
.hero{min-height:100svh;padding:110px 5vw 50px;display:flex;flex-direction:column;justify-content:center;position:relative;overflow:hidden}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#1c140f 35%,#1c140f55),url(photo.jpg) right/cover;z-index:-1}
.hero h1{font:700 clamp(80px,14vw,230px)/.88 'Oswald';text-transform:uppercase}.hero h1 span{color:#ff6a2b}
.hero p{max-width:36ch;margin:22px 0 30px;font-size:19px}
.board{background:#0b0806;padding:clamp(60px,9vw,120px) 5vw}
.fl{display:grid;gap:8px;margin-top:30px;font:500 clamp(16px,2.6vw,34px) 'IBM Plex Mono',monospace}
.row{display:flex;gap:4px;flex-wrap:wrap}.ch{width:1.05em;height:1.5em;display:inline-grid;place-items:center;background:#1f1a16;border-radius:4px;color:#ffd166;position:relative;box-shadow:inset 0 -1px 0 #000;text-transform:uppercase}
.ch::after{content:"";position:absolute;left:0;right:0;top:50%;height:1px;background:#000a}
.mn{padding:clamp(70px,11vw,140px) 5vw;display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px}
.mn .tg{border:1.5px solid #ff6a2b55;border-radius:18px;padding:24px;font:400 30px 'Oswald';letter-spacing:.03em;transition:.3s}.mn .tg:hover{background:#ff6a2b;color:#1c140f}
@media(max-width:860px){.hero::after{background:linear-gradient(#1c140fcc,#1c140f),url(photo.jpg) center/cover}}'''
    atts=[a for a in o['attrs'] if not a.startswith('Чек')]
    body=f'''<nav><span style="display:flex;gap:12px;align-items:center"><img src="logo.jpg" alt="Логотип «Всегда кофе»"><b>Всегда кофе</b></span><a class="btn" data-mag href="#visit">Позвонить</a></nav>
<header class="hero"><p class="cap">кофейня · Красногорский б-р, 20, 6 подъезд</p><h1>Всегда<br><span>кофе.</span></h1><p>Завтраки, сэндвичи, какао и молочные коктейли. Можно с ноутбуком. Средний чек — 700 ₽.</p><div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn" data-mag href="#visit">Как добраться</a><a class="btn o" href="tel:{o['tel']}">{E(o['phone'])}</a></div></header>
<section class="board"><p class="cap rv">табло отправлений · часы работы</p><div class="fl" id="fb" data-l="ПН–ПТ  08:30–20:30|СБ–ВС  10:00–21:00|ЧЕК       700 ₽"></div></section>
<section class="mn">{''.join(f'<div class="tg rv">{E(a)}</div>' for a in atts)}</section>
{tail(o,['Столик','Кофе с собой','Вопрос'],'Заходите')}
<script>(function(){{var b=document.getElementById('fb'),L=b.dataset.l.split('|'),A='АБВГДЕЖЗИКЛМНОПРСТУФХЧЦШЭЮЯ0123456789:–₽ ',R=matchMedia('(prefers-reduced-motion: reduce)').matches,cs=[];L.forEach(function(l){{var r=document.createElement('div');r.className='row';r.setAttribute('aria-label',l);[].forEach.call(l,function(c){{var s=document.createElement('span');s.className='ch';s.textContent=R?c:' ';s.dataset.c=c;r.appendChild(s);cs.push(s)}});b.appendChild(r)}});
if(R)return;var go=function(){{cs.forEach(function(s,i){{var n=0,m=6+i%9;var t=setInterval(function(){{s.textContent=++n>=m?s.dataset.c:A[Math.random()*A.length|0];if(n>=m)clearInterval(t)}},60)}})}};var io=new IntersectionObserver(function(e){{if(e[0].isIntersecting){{go();io.disconnect()}}}});io.observe(b);setTimeout(function(){{cs.forEach(function(s){{s.textContent=s.dataset.c}})}},6000)}})()</script>'''
    page(o,'vsegda-kofe','Всегда кофе — кофейня, Красногорский б-р, 20','family=Oswald:wght@500;700&family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Mono:wght@500',css,body)

@site
def n495():
    o=D[19]
    css=TC('#f2f0ea','#111','#2e4bff',"'Syne'",'#fff','#fff')+'''
body{background:#f2f0ea;color:#111;font:400 17px/1.6 'Inter',sans-serif}
nav{mix-blend-mode:normal}nav b{font:800 24px 'Syne'}
.hero{min-height:100svh;padding:100px 5vw 40px;display:grid;place-items:center;perspective:900px;overflow:hidden;position:relative}
.big{font:800 clamp(150px,30vw,460px)/.8 'Syne';letter-spacing:-.06em;display:flex;transform-style:preserve-3d}
.big span{display:inline-block;background:linear-gradient(135deg,#2e4bff,#111 70%);-webkit-background-clip:text;background-clip:text;color:transparent;transition:transform .2s ease-out}
.hero .ph{position:absolute;width:26vw;max-width:340px;aspect-ratio:3/4;object-fit:cover;border-radius:999px 999px 20px 20px;right:7vw;bottom:8vh;rotate:6deg;box-shadow:0 30px 60px -30px #000}
.hero .tx{position:absolute;left:5vw;bottom:8vh;max-width:34ch}.hero .tx{box-sizing:border-box}
.mq{overflow:hidden;background:#2e4bff;color:#fff;padding:18px 0;font:800 clamp(28px,4vw,54px) 'Syne';white-space:nowrap}
.mq div{display:inline-block;animation:mq 30s linear infinite}@keyframes mq{to{transform:translateX(-50%)}}
.mn{padding:clamp(70px,11vw,140px) 5vw}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:#1112;margin-top:40px;border:1px solid #1112}
.grid div{background:#f2f0ea;padding:26px 20px;font-weight:600;font-size:18px;transition:.3s}.grid div:hover{background:#2e4bff;color:#fff}
@media(max-width:860px){.hero .ph{position:relative;width:60vw;right:auto;bottom:auto;margin:20px auto 0}.hero .tx{position:static;margin-top:20px;max-width:100%;width:100%}.big{font-size:31vw;margin-top:4vh}.hero{place-items:start center}.grid{grid-template-columns:1fr 1fr}}'''
    atts=[a for a in o['attrs'] if not a.startswith('Чек')]
    body=f'''<nav><b>495</b><a class="btn" data-mag href="#visit">Позвонить</a></nav>
<header class="hero" id="h"><div class="big" id="bg" aria-label="495"><span>4</span><span>9</span><span>5</span></div><div class="tx"><p class="cap">кофейня · Красногорский б-р, 18</p><p style="font-size:19px;margin:12px 0 22px">Ежедневно с 8:00 до 21:00. Вафли, боулы, поке, вареники и кофе с собой. Средний чек — 700 ₽.</p><a class="btn" data-mag href="#menu">Что в меню</a></div><img class="ph" src="photo.jpg" alt="Кофейня 495"></header>
<div class="mq" aria-hidden="true"><div>{'  ·  '.join(atts*2)}  ·  </div></div>
<section class="mn" id="menu"><p class="cap rv">в меню · по данным 2ГИС</p><h2 class="h2 rv">{len(atts)} причины<br>зайти</h2><div class="grid">{''.join(f'<div class="rv">{E(a)}</div>' for a in atts)}</div><p style="margin-top:20px;opacity:.6">Цены уточняйте в кофейне. Средний чек по 2ГИС — 700 ₽.</p></section>
{tail(o,['Доставка','Столик','Вопрос'],'Заходите')}
<script>(function(){{if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;var s=[].slice.call(document.querySelectorAll('#bg span'));function m(x,y){{s.forEach(function(e,i){{e.style.transform='rotateY('+(x*24)+'deg) rotateX('+(-y*16)+'deg) translateY('+(Math.sin(i+x*3)*12)+'px)'}})}}addEventListener('pointermove',function(e){{m(e.clientX/innerWidth-.5,e.clientY/innerHeight-.5)}});var t=0;(function a(){{if(!matchMedia('(hover:hover)').matches){{t+=.02;m(Math.sin(t)*.4,Math.cos(t*.7)*.2)}}requestAnimationFrame(a)}})()}})()</script>'''
    page(o,'495','495 — кофейня, Красногорский б-р, 18','family=Syne:wght@800&family=Inter:wght@400;600',css,body)

@site
def prana():
    o=D[20]
    css=TC('#e9efe6','#24301f','#5b7a4a',"'Cormorant'",'#fff9','#fff')+'''
body{background:#e9efe6;color:#24301f;font:400 17px/1.7 'Nunito Sans',sans-serif}
nav{background:#e9efe6cc;backdrop-filter:blur(8px)}nav b{font:600 italic 26px 'Cormorant'}
.hero{min-height:100svh;display:grid;place-items:center;text-align:center;padding:110px 5vw 60px;position:relative;overflow:hidden}
.br{position:absolute;width:min(78vw,640px);aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,#c9d8bf 0,#c9d8bf00 70%);animation:br 8s ease-in-out infinite}
.br.b2{width:min(52vw,420px);background:radial-gradient(circle,#a9c09a 0,#a9c09a00 70%);animation-delay:-4s}
@keyframes br{0%,100%{transform:scale(.75);opacity:.6}50%{transform:scale(1.08);opacity:1}}
.hero>div{position:relative}.hero h1{font:500 clamp(70px,12vw,190px)/.9 'Cormorant';letter-spacing:-.01em}.hero h1 i{color:#5b7a4a}
.hero p{max-width:40ch;margin:20px auto 28px;font-size:18px}
.lbl{font:600 13px 'Nunito Sans';letter-spacing:.3em;text-transform:uppercase;margin-top:22px;height:20px}
.dy{display:grid;grid-template-columns:1fr 1fr;min-height:80vh}.dy img{width:100%;height:100%;object-fit:cover}
.dy div{padding:clamp(60px,9vw,120px) 5vw;align-self:center}
.tm{display:flex;gap:30px;margin-top:30px;flex-wrap:wrap}.tm b{display:block;font:500 54px/1 'Cormorant';color:#5b7a4a}
@media(max-width:860px){.dy{grid-template-columns:1fr}.dy img{height:50vh}}'''
    body=f'''<nav><b>Prana coffee</b><a class="btn" data-mag href="#visit">Написать</a></nav>
<header class="hero"><span class="br"></span><span class="br b2"></span><div><p class="cap">кофейня · Молодёжная ул., 3</p><h1>Вдох.<br><i>Кофе.</i></h1><p>Тихая точка на Молодёжной: кофе с собой с 7 утра в будни. Сделайте паузу вместе с кругом.</p><a class="btn" data-mag href="#visit">Как нас найти</a><p class="lbl" id="lb" aria-hidden="true">вдох</p></div></header>
<section class="dy"><img src="photo.jpg" alt="Prana coffee" loading="lazy"><div><p class="cap rv">ритм дня</p><h2 class="h2 rv">Раньше всех<br>на бульваре</h2><div class="tm rv"><div><b>07:00</b>открываемся в будни</div><div><b>08:00</b>в выходные</div><div><b>21:00</b>закрываемся</div></div><p class="rv" style="margin-top:26px">Кофе с собой — по данным 2ГИС. Цены и меню уточняйте на месте.</p></div></section>
{tail(o,['Кофе с собой','Вопрос'],'Заходите')}
<script>(function(){{var l=document.getElementById('lb');if(matchMedia('(prefers-reduced-motion: reduce)').matches){{l.remove();return}}var w=['вдох','выдох'],i=0;setInterval(function(){{l.textContent=w[++i%2]}},4000)}})()</script>'''
    page(o,'prana','Prana coffee — кофейня, Молодёжная ул., 3','family=Cormorant:ital,wght@0,500;1,500;1,600&family=Nunito+Sans:wght@400;600',css,body)

@site
def negrul():
    o=D[21]
    css=TC('#7a1f1a','#fbf1e1','#e3a72f',"'Ruslan Display'",'#ffffff10','#3a0f0c')+'''
body{background:#fbf1e1;color:#3a0f0c;font:400 17px/1.65 'PT Sans',sans-serif}
nav{background:#fbf1e1e6;backdrop-filter:blur(8px)}nav b{font:400 24px 'Ruslan Display';color:#7a1f1a}
.orn{height:34px;background:repeating-linear-gradient(45deg,#7a1f1a 0 8px,transparent 8px 16px),repeating-linear-gradient(-45deg,#e3a72f 0 8px,transparent 8px 16px);background-size:32px 34px;opacity:.9}
.js .orn{background-position:0 0;animation:op 12s linear infinite}@keyframes op{to{background-position:320px 0}}
.hero{min-height:100svh;padding:110px 5vw 50px;display:grid;grid-template-columns:1fr 1fr;gap:5vw;align-items:center}
.hero h1{font:400 clamp(52px,7.5vw,118px)/1 'Ruslan Display';color:#7a1f1a}
.hero p{margin:22px 0 30px;max-width:36ch;font-size:19px}
.fr{position:relative;padding:18px;background:#7a1f1a;border-radius:50% 50% 24px 24px/30% 30% 24px 24px}.fr img{border-radius:50% 50% 14px 14px/30% 30% 14px 14px;width:100%;aspect-ratio:4/5;object-fit:cover}
.fr::before{content:"✦ ✦ ✦";position:absolute;top:-30px;left:0;right:0;text-align:center;color:#e3a72f;font-size:22px;letter-spacing:.6em}
.mn{background:#7a1f1a;color:#fbf1e1;padding:clamp(70px,11vw,140px) 5vw}
.dish{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:40px}
.dish div{border:2px solid #e3a72f;border-radius:999px 999px 20px 20px;padding:40px 20px 26px;text-align:center;font:700 21px 'PT Sans';transition:.4s}.dish div:hover{background:#e3a72f;color:#3a0f0c;transform:translateY(-6px)}
.dish div span{display:block;font-size:40px;margin-bottom:10px}
@media(max-width:860px){.hero{grid-template-columns:1fr}.hero h1{font-size:10.5vw}.dish{grid-template-columns:1fr 1fr}}'''
    d=[('🥟','Пельмени'),('🥧','Пирожки'),('🥗','Салаты'),('🍲','Супы'),('🍳','Поздний завтрак'),('☕','Кофе с собой'),('🛵','Доставка'),('🧾','Чек ≈ 800 ₽')]
    body=f'''<nav><b>Эйфория</b><a class="btn" data-mag href="#visit">Позвонить</a></nav>
<header class="hero"><div><p class="cap">кафе-кондитерская «Негруль» · Красногорский б-р, 19</p><h1>По-домашнему<br>вкусно</h1><p>Пельмени, пирожки, супы и салаты. Ежедневно с 9:00 до 21:00, есть доставка. Средний чек — около 800 ₽.</p><div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn" data-mag href="#visit">Заказать</a><a class="btn o" href="tel:{o['tel']}">{E(o['phone'])}</a></div></div><div class="fr"><img src="photo.jpg" alt="Кафе на Красногорском б-ре, 19"></div></header>
<div class="orn" aria-hidden="true"></div>
<section class="mn"><p class="cap rv">меню · по данным 2ГИС</p><h2 class="h2 rv" style="font-family:'Ruslan Display'">На столе</h2><div class="dish">{''.join(f'<div class="rv"><span aria-hidden="true">{a}</span>{b}</div>' for a,b in d)}</div><p style="margin-top:22px;opacity:.7">Цены отдельных блюд — уточняйте в кафе.</p></section>
<div class="orn" aria-hidden="true"></div>
{tail(o,['Заказ с доставкой','Столик','Вопрос'],'Заказ')}'''
    page(o,'negrul','Негруль («Эйфория») — кафе, Красногорский б-р, 19','family=Ruslan+Display&family=PT+Sans:wght@400;700',css,body)

@site
def popnails():
    o=D[22]
    css=TC('#ffe600','#111','#ff2e88',"'Rubik Mono One'",'#fff','#fff','0')+'''
body{background:#ffe600;color:#111;font:500 17px/1.6 'Rubik',sans-serif}
nav{background:#111;color:#ffe600}nav b{font:400 20px 'Rubik Mono One'}.btn{box-shadow:5px 5px 0 #111;border:2.5px solid #111!important}
.hero{min-height:100svh;padding:110px 5vw 50px;display:grid;grid-template-columns:1.1fr 1fr;gap:4vw;align-items:center;background-image:radial-gradient(#ff2e8866 2px,transparent 2.5px);background-size:16px 16px}
.hero h1{font:400 clamp(54px,8.5vw,140px)/.95 'Rubik Mono One';-webkit-text-stroke:3px #111;color:#fff;text-shadow:8px 8px 0 #ff2e88}
.hero p{margin:22px 0 30px;max-width:34ch;font-size:19px;background:#fff;border:2.5px solid #111;padding:16px 20px;box-shadow:6px 6px 0 #111;border-radius:22px 22px 22px 0}
.pc{position:relative;border:4px solid #111;box-shadow:14px 14px 0 #111;rotate:-3deg;overflow:hidden}.pc img{width:100%;aspect-ratio:4/5;object-fit:cover;filter:contrast(1.15) saturate(1.3)}
.pc::after{content:"";position:absolute;inset:0;background:radial-gradient(#ff2e88 1.4px,transparent 1.8px) 0 0/7px 7px;mix-blend-mode:multiply;opacity:.5}
.pow{position:absolute;right:-10px;top:-10px;background:#ff2e88;color:#fff;font:400 22px 'Rubik Mono One';padding:30px 26px;clip-path:polygon(50% 0,61% 30%,98% 20%,72% 50%,100% 80%,62% 70%,50% 100%,38% 70%,0 80%,28% 50%,2% 20%,39% 30%);z-index:2}
.sv{padding:clamp(70px,11vw,140px) 5vw;background:#111;color:#fff}
.bb{display:flex;flex-wrap:wrap;gap:20px;margin-top:40px}
.bb button{font:400 clamp(16px,2vw,22px) 'Rubik Mono One';padding:28px 34px;border-radius:50%/60%;border:3px solid #fff;background:#ff2e88;color:#fff;cursor:pointer;transition:transform .2s}
.bb button:nth-child(2n){background:#2ec4ff;color:#111}.bb button:nth-child(3n){background:#ffe600;color:#111}
.bb button.p{animation:pop .45s}@keyframes pop{40%{transform:scale(1.25) rotate(-6deg)}70%{transform:scale(.9)}}
.s-rv{background:#fff}.q{box-shadow:6px 6px 0 #111;border:2.5px solid #111!important;border-radius:0!important}
@media(max-width:860px){.hero{grid-template-columns:1fr}.hero h1{-webkit-text-stroke:2px #111;text-shadow:5px 5px 0 #ff2e88}}'''
    sv=['Аппаратный маникюр','Гель-лак','Женский педикюр','Мужской маникюр','Брови','Ресницы']
    body=f'''<nav><b>POPNAILS</b><a class="btn" data-mag href="#visit">Записаться</a></nav>
<header class="hero"><div><p class="cap">студия красоты · Красногорский б-р, 18</p><h1>POP!<br>NAILS</h1><p>Маникюр, педикюр, брови и ресницы — каждый день с 10 до 22. Рейтинг {rating(o)} ★ в 2ГИС.</p><div style="display:flex;gap:14px;flex-wrap:wrap"><a class="btn" data-mag href="#visit">Записаться</a><a class="btn o" style="background:#fff" href="tel:{o['tel']}">{E(o['phone'])}</a></div></div><div class="pc"><span class="pow">{rating(o)}★</span><img src="photo.jpg" alt="Работа Popnails"></div></header>
<section class="sv"><p class="cap rv">услуги · жми на пузырь</p><h2 class="h2 rv">Выбирай<br>свой поп</h2><div class="bb">{''.join(f'<button class="rv" type="button" data-s="{E(a)}">{E(a)}</button>' for a in sv)}</div><p style="margin-top:26px;opacity:.7">Стоимость — по записи. Нажмите на услугу, и она подставится в форму.</p></section>
{tail(o,sv)}
<script>document.querySelectorAll('.bb button').forEach(function(b){{b.addEventListener('click',function(){{b.classList.remove('p');void b.offsetWidth;b.classList.add('p');var s=document.querySelector('#visit select');s.value=b.dataset.s;setTimeout(function(){{document.getElementById('visit').scrollIntoView({{behavior:'smooth'}})}},420)}})}})</script>'''
    page(o,'popnails','Popnails — студия красоты, Красногорский б-р, 18','family=Rubik+Mono+One&family=Rubik:wght@500;700',css,body)

@site
def mindal():
    o=D[23]
    css=TC('#fbf3ee','#4a2e2a','#c98b7b',"'Lora'",'#fff','#fff')+'''
body{background:#fbf3ee;color:#4a2e2a;font:400 17px/1.7 'Jost',sans-serif}
nav{background:#fbf3eecc;backdrop-filter:blur(8px)}nav b{font:500 italic 26px 'Lora'}
.hero{min-height:100svh;position:relative;display:grid;grid-template-columns:1fr 1fr;align-items:center;padding:100px 5vw 50px;gap:5vw;overflow:hidden}
#pt{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:1}
.hero>div,.hero>figure{position:relative;z-index:2}
.hero h1{font:400 clamp(64px,10vw,160px)/.92 'Lora';letter-spacing:-.02em}.hero h1 em{color:#c98b7b}
.hero p{margin:20px 0 30px;max-width:34ch;font-size:18px}
.hero figure{margin:0;border-radius:999px;overflow:hidden;aspect-ratio:1;max-width:520px;justify-self:center;border:10px solid #fff;box-shadow:0 40px 80px -40px #c98b7b}
.hero figure img{width:100%;height:100%;object-fit:cover}
.sv{padding:clamp(70px,11vw,140px) 5vw;background:#f3e2d9}
.pl{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:40px}
.pl div{background:#fff;padding:34px 24px;border-radius:120px 120px 24px 24px;text-align:center;transition:transform .5s}.pl div:hover{transform:translateY(-8px) rotate(-1.5deg)}
.pl h3{font:500 24px/1.15 'Lora';margin:14px 0 8px}.pl i{font-size:30px;font-style:normal}
@media(max-width:860px){.hero{grid-template-columns:1fr}.pl{grid-template-columns:1fr 1fr}.hero figure{max-width:80vw}}'''
    sv=['Аппаратный маникюр','Гель-лак','Женский педикюр','Мужской маникюр']
    body=f'''<nav><b>Миндаль</b><a class="btn" data-mag href="#visit">Записаться</a></nav>
<header class="hero"><canvas id="pt" aria-hidden="true"></canvas><div><p class="cap">ногтевая студия · Красногорский б-р, 19</p><h1>Нежность<br><em>миндаля</em></h1><p>Аккуратная форма, мягкие оттенки, спокойная атмосфера. Ежедневно 10:00–22:00 · {rating(o)} ★ в 2ГИС.</p><div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn" data-mag href="#visit">Выбрать время</a><a class="btn o" href="tel:{o['tel']}">{E(o['phone'])}</a></div></div><figure><img src="photo.jpg" alt="Работа студии Миндаль"></figure></header>
<section class="sv"><p class="cap rv">услуги · по данным 2ГИС</p><h2 class="h2 rv">Для ваших рук</h2><div class="pl">{''.join(f'<div class="rv"><i aria-hidden="true">✿</i><h3>{a}</h3><p>по записи</p></div>' for a in sv)}</div></section>
{tail(o,sv)}
<script>(function(){{var c=document.getElementById('pt'),x=c.getContext('2d');if(matchMedia('(prefers-reduced-motion: reduce)').matches){{c.remove();return}}var P=[],W,H;function sz(){{var d=Math.min(2,devicePixelRatio||1);W=c.offsetWidth;H=c.offsetHeight;c.width=W*d;c.height=H*d;x.setTransform(d,0,0,d,0,0)}}sz();addEventListener('resize',sz);
for(var i=0;i<(innerWidth<700?18:36);i++)P.push({{x:Math.random(),y:Math.random(),s:6+Math.random()*10,v:.0006+Math.random()*.001,r:Math.random()*6,w:Math.random()*6}});
(function f(){{x.clearRect(0,0,W,H);P.forEach(function(p){{p.y+=p.v;p.r+=.01;p.w+=.02;if(p.y>1.05)p.y=-.05;x.save();x.translate((p.x+Math.sin(p.w)*.02)*W,p.y*H);x.rotate(p.r);x.fillStyle='rgba(232,170,160,.55)';x.beginPath();x.ellipse(0,0,p.s,p.s*.55,0,0,7);x.fill();x.restore()}});requestAnimationFrame(f)}})()}})()</script>'''
    page(o,'mindal','Миндаль — ногтевая студия, Красногорский б-р, 19','family=Lora:ital,wght@0,400;0,500;1,400;1,500&family=Jost:wght@400;500',css,body)

@site
def territoriya():
    o=D[24]
    css=TC('#0f2a2a','#e9f1ee','#3fd0a6',"'Tenor Sans'",'#ffffff0a','#0f2a2a')+'''
body{background:#0f2a2a;color:#e9f1ee;font:400 17px/1.65 'Manrope',sans-serif}
nav{background:#0f2a2acc;backdrop-filter:blur(8px)}nav b{font:400 22px 'Tenor Sans';letter-spacing:.1em}
.hero{min-height:100svh;padding:110px 5vw 50px;display:grid;grid-template-columns:1.1fr 1fr;gap:5vw;align-items:center;position:relative;overflow:hidden}
.topo{position:absolute;inset:0;width:100%;height:100%;opacity:.35;z-index:0}.topo path{fill:none;stroke:#3fd0a6;stroke-width:1}
.js .topo path{stroke-dasharray:1400;stroke-dashoffset:1400;animation:dr 6s ease forwards}@keyframes dr{to{stroke-dashoffset:0}}
.hero>*:not(svg){position:relative;z-index:1}
.hero h1{font:400 clamp(50px,7.5vw,118px)/.98 'Tenor Sans'}.hero h1 span{color:#3fd0a6}
.hero p{margin:22px 0 30px;max-width:36ch;font-size:18px;opacity:.85}
.hero img{border-radius:30px;aspect-ratio:4/5;object-fit:cover;width:100%;max-width:480px;justify-self:end}
.pr{padding:clamp(70px,11vw,140px) 5vw;background:#e9f1ee;color:#0f2a2a}
.pr .svc li{display:grid;grid-template-columns:auto 1fr auto;gap:22px;align-items:baseline;padding:24px 0;border-bottom:1px solid #0f2a2a22;font-size:clamp(18px,2vw,24px)}
.pr .svc li::before{content:attr(data-n);font:400 14px 'Tenor Sans';color:#2a9f7d}.pr .svc b{font-weight:700;white-space:nowrap}
@media(max-width:860px){.hero{grid-template-columns:1fr}.hero img{justify-self:start}}'''
    paths=''.join(f'<path d="M-50 {120+i*70} C 300 {60+i*70}, 500 {220+i*70}, 800 {130+i*70} S 1300 {40+i*70}, 1550 {160+i*70}" style="animation-delay:{i*.25}s"/>' for i in range(10))
    rows=o['prices']
    body=f'''<nav><b>ТЕРРИТОРИЯ</b><a class="btn" data-mag href="#visit">Записаться</a></nav>
<header class="hero"><svg class="topo" viewBox="0 0 1500 900" preserveAspectRatio="none" aria-hidden="true">{paths}</svg><div><p class="cap">студия ногтевого сервиса · {E(o['addr'].replace('Красногорск, ',''))}</p><h1>Территория<br><span>здоровых</span><br>ногтей</h1><p>Маникюр, педикюр и подология: вросший ноготь, онихолизис, мазоли, коррекция системой Light System. {rating(o)} ★ в 2ГИС.</p><div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn" data-mag href="#visit">Записаться</a><a class="btn o" href="#price">Цены</a></div></div><img src="photo.jpg" alt="Студия «Территория маникюра»"></header>
<section class="pr" id="price"><p class="cap rv">подология · онлайн-запись DIKIDI</p><h2 class="h2 rv">Карта услуг</h2><ul class="svc">{''.join(f'<li class="rv" data-n="{i+1:02d}"><span>{E(a)}</span><b>{E(b)}</b></li>' for i,(a,b) in enumerate(rows))}</ul><p style="margin-top:20px;opacity:.6">Цены — из онлайн-записи студии. Маникюр и педикюр — стоимость по записи.</p></section>
{tail(o,[a for a,b in rows]+['Маникюр','Педикюр'])}'''
    page(o,'territoriya-manikyura','Территория маникюра — студия ногтевого сервиса','family=Tenor+Sans&family=Manrope:wght@400;700',css,body)

@site
def yourmed():
    o=D[25]
    css=TC('#f4f8fc','#0b2545','#0a7cff',"'Manrope'",'#fff','#fff')+'''
body{background:#f4f8fc;color:#0b2545;font:400 17px/1.65 'Manrope',sans-serif}
nav{background:#f4f8fcd9;backdrop-filter:blur(10px)}nav img{height:38px;border-radius:8px}
.hero{min-height:100svh;padding:110px 5vw 40px;display:grid;grid-template-columns:1.1fr 1fr;gap:5vw;align-items:center}
.hero h1{font:800 clamp(46px,6.8vw,104px)/1 'Manrope';letter-spacing:-.04em}.hero h1 span{color:#0a7cff}
.hero p{margin:22px 0 30px;max-width:38ch;font-size:19px}
.card{background:#fff;border-radius:32px;padding:14px;box-shadow:0 40px 80px -40px #0b254555}.card img{border-radius:22px;width:100%;aspect-ratio:4/3;object-fit:cover}
.ecg{height:70px;margin-top:10px}.ecg path{fill:none;stroke:#0a7cff;stroke-width:3;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:900;stroke-dashoffset:900;animation:ecg 3s linear infinite}@keyframes ecg{to{stroke-dashoffset:-900}}
.kp{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:22px}.kp div{background:#fff;border-radius:20px;padding:20px}.kp b{display:block;font:800 36px 'Manrope';color:#0a7cff}
.dp{padding:clamp(70px,11vw,140px) 5vw;background:#0b2545;color:#fff}
.dg{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:40px}.dg div{border:1px solid #ffffff22;border-radius:22px;padding:28px 22px;font-weight:700;font-size:20px;transition:.3s}.dg div:hover{background:#0a7cff;border-color:#0a7cff}
.dg div::before{content:"+";display:block;font-size:30px;color:#4da3ff;margin-bottom:12px}
@media(max-width:860px){.hero h1{font-size:11vw}.kp b{font-size:26px}.kp div{padding:14px;font-size:13px}.hero{grid-template-columns:1fr}.dg{grid-template-columns:1fr 1fr}}'''
    dp=['Многопрофильный приём','Медицинская диагностика','Детские врачи','Гинеколог']
    body=f'''<nav><img src="logo.jpg" alt="YourMed"><a class="btn" data-mag href="#visit">Записаться</a></nav>
<header class="hero"><div><p class="cap">медцентр для всей семьи · ЖК ART, Авангардная ул., 3</p><h1>Врачи для всей<br><span>семьи</span> — рядом с домом</h1><p>Взрослые и детские специалисты, диагностика и гинекология. Пн–Пт 8:00–21:00, Сб–Вс 9:00–21:00.</p><div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn" data-mag href="#visit">Записаться на приём</a><a class="btn o" href="tel:{o['tel']}">{E(o['phone'])}</a></div>
<div class="kp"><div><b>{rating(o)}</b>★ в 2ГИС, {o['cnt']} оценок</div><div><b>12</b>филиалов сети</div><div><b>7/7</b>без выходных</div></div></div>
<div class="card"><img src="photo.jpg" alt="Медцентр YourMed в Красногорске"><svg class="ecg" viewBox="0 0 600 70" preserveAspectRatio="none" aria-hidden="true"><path d="M0 40 H170 L190 40 L205 10 L222 64 L238 28 L250 40 H380 L395 40 L410 18 L425 56 L438 40 H600"/></svg></div></header>
<section class="dp"><p class="cap rv">направления · по данным 2ГИС</p><h2 class="h2 rv">Чем поможем</h2><div class="dg">{''.join(f'<div class="rv">{a}</div>' for a in dp)}</div><p style="margin-top:22px;opacity:.7">Стоимость приёма — по записи или на сайте клиники.</p></section>
{tail(o,dp,'Запись на приём')}'''
    page(o,'yourmed','YourMed — медцентр для всей семьи, Красногорск','family=Manrope:wght@400;700;800',css,body)

@site
def gruzinskie():
    o=D[26]
    css=TC('#1b120d','#f7ecdc','#b3262d',"'Lobster'",'#ffffff0a','#fff')+'''
body{background:#1b120d;color:#f7ecdc;font:400 17px/1.65 'Fira Sans',sans-serif}
nav{background:#1b120dcc;backdrop-filter:blur(10px)}nav b{font:400 26px 'Lobster'}
.hero{min-height:100svh;position:relative;overflow:hidden;display:flex;align-items:flex-end;padding:0 5vw 10vh}
.hero .bg{position:absolute;inset:-10% 0 0;background:url(photo.jpg) center/cover;filter:brightness(.55)}
.mt{position:absolute;left:0;right:0;bottom:0;width:100%;will-change:transform}
.hero .tx{position:relative;z-index:3;max-width:900px}
.hero h1{font:400 clamp(64px,10vw,170px)/.95 'Lobster';text-shadow:0 10px 40px #0008}
.hero p{margin:18px 0 28px;max-width:40ch;font-size:19px}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:20px}.chips span{background:#f7ecdc;color:#1b120d;padding:8px 16px;border-radius:999px;font-weight:600;font-size:14px}
.mn{padding:clamp(70px,11vw,140px) 5vw;background:#f7ecdc;color:#1b120d}
.dish{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px;margin-top:40px}
.dish div{background:#fff;border-radius:24px;padding:26px;font-weight:700;font-size:20px;border-bottom:5px solid #b3262d;transition:.35s}.dish div:hover{transform:translateY(-6px) rotate(-1deg)}
.kf{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:30px}.kf div{background:#b3262d;color:#fff;border-radius:24px;padding:26px}.kf b{display:block;font:400 46px/1 'Lobster'}
@media(max-width:860px){.kf{grid-template-columns:1fr}}'''
    dishes=['Хинкали','Хачапури','Шашлык','Люля-кебаб','На гриле','Плов','Супы','Салаты','Шаурма']
    body=f'''<nav><b>Грузинские каникулы</b><a class="btn" data-mag href="#visit">Забронировать</a></nav>
<header class="hero"><div class="bg" id="pbg"></div>
<svg class="mt" id="m1" viewBox="0 0 1440 320" preserveAspectRatio="none" aria-hidden="true" style="height:42vh;z-index:1"><path fill="#3b2a20" d="M0 320 L0 190 L160 90 L300 170 L470 40 L640 160 L800 70 L980 180 L1150 60 L1300 150 L1440 100 L1440 320Z"/><path fill="#fff" opacity=".85" d="M470 40 L430 75 L470 66 L505 80Z M1150 60 L1110 95 L1150 86 L1185 98Z M800 70 L770 96 L800 90 L828 100Z"/></svg>
<svg class="mt" id="m2" viewBox="0 0 1440 320" preserveAspectRatio="none" aria-hidden="true" style="height:30vh;z-index:2"><path fill="#1b120d" d="M0 320 L0 230 L220 150 L420 230 L620 140 L860 240 L1060 160 L1260 230 L1440 170 L1440 320Z"/></svg>
<div class="tx"><p class="cap">ресторан домашней кухни · Павшинский б-р, 20а</p><h1>Гамарджоба,<br>Павшино!</h1><p>Хинкали, хачапури и шашлык на гриле. Летняя веранда, доставка и бизнес-ланч от 390 ₽. {rating(o)} ★ — {o['cnt']} оценок в 2ГИС.</p><div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn" data-mag href="#visit">Забронировать стол</a><a class="btn o" href="tel:{o['tel']}">{E(o['phone'])}</a></div><div class="chips"><span>Номинант 2026 · 2ГИС</span><span>Летняя веранда</span><span>Доставка</span></div></div></header>
<section class="mn"><p class="cap rv">меню · по данным 2ГИС</p><h2 class="h2 rv" style="font-family:Lobster">Со стола<br>в Тбилиси</h2><div class="dish">{''.join(f'<div class="rv">{a}</div>' for a in dishes)}</div>
<div class="kf"><div class="rv"><b>от 390 ₽</b>бизнес-ланч</div><div class="rv"><b>1 100 ₽</b>средний чек</div><div class="rv"><b>11:00</b>открываемся ежедневно</div></div></section>
{tail(o,['Бронь стола','Доставка','Банкет'],'Бронь')}
<script>(function(){{if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;var a=document.getElementById('m1'),b=document.getElementById('m2'),g=document.getElementById('pbg');addEventListener('scroll',function(){{var y=scrollY;if(y>innerHeight*1.2)return;g.style.transform='translateY('+y*.4+'px)';a.style.transform='translateY('+y*.18+'px)';b.style.transform='translateY('+y*.05+'px)'}},{{passive:true}})}})()</script>'''
    page(o,'gruzinskie-kanikuly','Грузинские каникулы — ресторан, Павшинский б-р, 20а','family=Lobster&family=Fira+Sans:wght@400;600;700',css,body)

@site
def lakmi():
    o=D[27]
    css=TC('#120a1f','#f6ecff','#ff3df2',"'Unbounded'",'#ffffff08','#120a1f')+'''
body{background:#120a1f;color:#f6ecff;font:400 17px/1.6 'Golos Text',sans-serif}
nav{background:#120a1fcc;backdrop-filter:blur(10px)}nav b{font:800 22px 'Unbounded';color:#ff3df2;text-shadow:0 0 14px #ff3df2}
.hero{min-height:100svh;padding:110px 5vw 50px;display:grid;grid-template-columns:1.1fr 1fr;gap:5vw;align-items:center;position:relative;overflow:hidden}
.hero h1{font:800 clamp(60px,10vw,170px)/.9 'Unbounded';letter-spacing:-.04em;color:#fff;text-shadow:0 0 30px #ff3df2aa}
.drip{position:relative;display:inline-block}.drip i{position:absolute;top:82%;width:.12em;border-radius:0 0 999px 999px;background:#ff3df2;box-shadow:0 0 14px #ff3df2;height:0}
.js .drip i{animation:dp 3.2s cubic-bezier(.5,0,.3,1) forwards}@keyframes dp{to{height:var(--h)}}
.hero p{margin:30px 0 30px;max-width:34ch;font-size:19px}
.hero img{border-radius:40px;aspect-ratio:4/5;object-fit:cover;width:100%;max-width:460px;border:2px solid #ff3df2;box-shadow:0 0 60px -10px #ff3df2}
.pr{padding:clamp(70px,11vw,140px) 5vw}
.pr .svc li{display:grid;grid-template-columns:1fr auto;gap:20px;padding:22px 0;border-bottom:1px solid #ffffff22;font-size:clamp(17px,2vw,23px)}.pr .svc b{color:#ff3df2;white-space:nowrap}
@media(max-width:860px){.hero{grid-template-columns:1fr}}'''
    rows=o['prices']
    body=f'''<nav><b>Лак Ми</b><a class="btn" data-mag href="#visit">Записаться</a></nav>
<header class="hero"><div><p class="cap">студия маникюра · Молодёжная ул., 3</p><h1><span class="drip">Лак<i style="left:18%;--h:.5em;animation-delay:.4s"></i><i style="left:62%;--h:.85em;animation-delay:.9s"></i></span><br><span class="drip">Ми<i style="left:30%;--h:.65em;animation-delay:1.3s"></i></span></h1><p>Маникюр, педикюр и брови. Ежедневно с 10 до 22. {rating(o)} ★ в 2ГИС, 4,9 ★ (170 отзывов) в онлайн-записи DIKIDI.</p><div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn" data-mag href="#visit">Записаться</a><a class="btn o" href="#price">Прайс</a></div></div><img src="photo.jpg" alt="Студия Лак Ми"></header>
<section class="pr" id="price"><p class="cap rv">брови · онлайн-запись DIKIDI</p><h2 class="h2 rv">Прайс</h2><ul class="svc">{''.join(f'<li class="rv"><span>{E(a)}</span><b>{E(b)}</b></li>' for a,b in rows)}</ul><p style="margin-top:20px;opacity:.6">Маникюр и педикюр — стоимость по записи.</p></section>
{tail(o,['Маникюр','Педикюр']+[a for a,b in rows])}'''
    page(o,'lak-mi','Лак Ми — студия маникюра, Молодёжная ул., 3','family=Unbounded:wght@800&family=Golos+Text:wght@400;600',css,body)

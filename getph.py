import re,json,os,subprocess
ix=json.load(open('_raw/idx.json'))
out={}
for i,r in enumerate(ix):
    slug=r[1];h=open(f'_raw/{i:02d}/p.html',errors='ignore').read()
    ids=[]
    for m in re.finditer(r'https://i\d\.photo\.2gis\.com/images/(?:profile|branch)/[\w/]*?(\d+_\d+)\.jpg',h):
        u=m.group(0)
        if u not in ids: ids.append(u)
    ids=ids[:6];os.makedirs(f'{slug}/st',exist_ok=True);got=[]
    for k,u in enumerate(ids):
        p=f'{slug}/st/{k}.jpg';uu=u[:-4]+'_640x.jpg'
        if subprocess.run(['curl','-sfL','-m','8','-o',p,uu]).returncode==0 and os.path.getsize(p)>8000: got.append(p.split('/',1)[1])
        elif os.path.exists(p): os.remove(p)
    out[slug]=got;print(i,slug,len(got))
json.dump(out,open('_raw/stories.json','w'))

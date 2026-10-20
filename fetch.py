import openpyxl,re,json,subprocess,os
from PIL import Image
wb=openpyxl.load_workbook('/home/box/agent-data/agents/aa958351-6340-4885-82e6-1000b140a538/attachments/1cd8ea5767bb533182f091cdf31dc33391ab9083f9a303bf588b058802a2578c.xlsx')
rows=list(wb['Лиды Павшинская пойма'].iter_rows(values_only=True))[1:]
out=[]
for i,r in enumerate(rows):
    fid=r[8].rsplit('/',1)[1]; d=f'_raw/{i:02d}'; os.makedirs(d,exist_ok=True)
    subprocess.run(['curl','-sL','-m','20','-A','Mozilla/5.0',r[8],'-o',d+'/p.html'])
    h=open(d+'/p.html',errors='ignore').read()
    soc=sorted(set(re.findall(r'"type":"(vkontakte|instagram|telegram|website|whatsapp|youtube)","value":"([^"]+)"',h)))
    m=re.search(r'"main_photo_url":"(https://i\d\.photo\.2gis\.com/main/branch/[^"]+)"',h)
    cols=[];photo=None
    if m:
        subprocess.run(['curl','-sL','-m','20',m.group(1),'-o',d+'/main.jpg'])
        try:
            im=Image.open(d+'/main.jpg').convert('RGB');photo=im.size
            q=im.resize((80,80)).quantize(5);pal=q.getpalette()[:15]
            cols=['#%02x%02x%02x'%tuple(pal[k:k+3]) for k in range(0,15,3)]
        except Exception as e: photo=None
    out.append(dict(i=i,name=r[2],fid=fid,soc=soc,photo=photo,cols=cols))
    print(i,r[2],soc,photo,cols)
json.dump(out,open('_raw/meta.json','w'),ensure_ascii=False)

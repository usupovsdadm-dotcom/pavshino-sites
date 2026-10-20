import sys;from PIL import Image
ss=sys.argv[2:];out=sys.argv[1]
S=Image.new('RGB',(len(ss)*(720+195),450),'white');x=0
for s in ss:
  for v,w in (('d',720),('m',195)):
    im=Image.open(f'_shots/{s}_{v}.png').convert('RGB').resize((w,450));S.paste(im,(x,0));x+=w
S.save(out)

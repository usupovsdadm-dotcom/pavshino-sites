cd /workspace/pavshino_sites
for d in */; do s=${d%/}; [ -f $s/index.html ] || continue
 for v in "390,844 m" "1440,900 d" "390,4200 mfull"; do set -- $v
  timeout 40 google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --window-size=$1 --virtual-time-budget=2500 --screenshot=_shots/${s}_$2.png "file://$PWD/$s/index.html?shot" 2>/dev/null >/dev/null
 done; echo $s; done

s=$1; cd /workspace/pavshino_sites
for v in "390,844 m" "1440,900 d"; do set -- $v; timeout 40 google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --user-data-dir=/tmp/cr_$s_$RANDOM --disable-application-cache --disk-cache-size=1 --window-size=$1 --virtual-time-budget=4000 --screenshot=_shots/${s}_$2.png "file://$PWD/$s/index.html?shot" >/dev/null 2>&1; done

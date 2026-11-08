q() { python -c "import urllib.parse,sys;print(urllib.parse.quote_plus(sys.argv[1]))" "$1"; }
call() {
  local f s e code; f=$(mktemp); s=$(date +%s)
  code=$(curl -s -m 150 -o "$f" -w "%{http_code}" "http://127.0.0.1:7000$1"); e=$(date +%s)
  printf '%s\t%s\t%ss\t%sB\t%s\n' "$(date +%H:%M:%S)" "$code" "$((e-s))" "$(wc -c <"$f")" "$1" >> "$OUT/calls.log"
  cat "$f"; rm -f "$f"
}
search()  { call "/$1/search?text=$(q "$2")&limit=${3:-8}"; }
extract() { call "/extract?url=$(q "$1")&mode=auto"; }

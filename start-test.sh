set -exuo pipefail

hyperfine --version
hyperfine --runs 30 --warmup 5 \
 --prepare "$PWD/start-app.sh && sleep 5" \
 'curl localhost:8000/pdf-uno/' \
 --prepare "pkill soffice || true" \
 'curl localhost:8000/pdf-subprocess/'
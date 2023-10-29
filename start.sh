set -exuo pipefail
hyperfine --version
#hyperfine --runs 80 --warmup 5 'soffice --convert-to pdf sample-docx-file-for-testing.docx' 'soffice --headless --convert-to pdf sample-docx-file-for-testing.docx'
hyperfine --runs 30 --warmup 5 \
 --prepare "soffice --accept='socket,host=localhost,port=2002;urp;StarOffice.Service' --headless & sleep 5" \
 'python convert-pdf-uno.py' \
 --prepare "pkill soffice || true" \
 'python convert-pdf-subprocess.py'
# 'soffice --convert-to pdf sample-docx-file-for-testing.docx' \
# --show-output
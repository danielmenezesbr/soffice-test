set -exuo pipefail
hyperfine --version
hyperfine --runs 20 --warmup 3 'soffice --convert-to pdf sample-docx-file-for-testing.docx' 'soffice --headless --convert-to pdf sample-docx-file-for-testing.docx'
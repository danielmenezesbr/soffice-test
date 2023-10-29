set -exu pipefail

export PYTHONPATH=/usr/lib/python3/dist-packages
pkill soffice || true
soffice --accept='socket,host=localhost,port=2002;urp;StarOffice.Service' --headless &
pkill -9 -f "uvicorn app:app --host localhost --port 8000" || true
uvicorn app:app --host localhost --port 8000 &
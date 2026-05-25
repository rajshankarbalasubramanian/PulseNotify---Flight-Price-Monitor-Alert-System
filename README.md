# PulseNotify---Flight-Price-Monitor-Alert-System

# PulseNotify

Flight price alert backend with Celery async notifications.

## Setup
```bash
docker compose up -d
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate --settings=pulsenotify.settings.local



---

##  Your Next Actions
1. Install Celery (`pip install celery[redis]`) so worker/beat commands run.  
2. Confirm all endpoints are working in Postman.  
3. Export the Postman collection.  
---



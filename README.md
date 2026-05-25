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
4. Write README.md with setup/run/test instructions.  
5. Push everything to GitHub.

---

Would you like me to generate a **ready-to-import Postman collection JSON** for the 13 scenarios so you can drop it straight into your repo without manually building each request?

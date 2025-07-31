import os
from datetime import datetime

USAGE_FILE = "data/api_usage.txt"
MAX_CALL_PER_DAY = 66

def load_api_usage():
   if not os.path.exists(USAGE_FILE):
        return {"date": str(datetime.today().date()), "count": 0}
   try:
        with open(USAGE_FILE, "r") as f:
            line = f.read().strip()
            date, count = line.split(",")
            return {"date": date, "count": int(count)}
   except Exception:
        # Corrupted file — reset usage
        return {"date": str(datetime.today().date()), "count": 0} 

def save_api_usage(usage):
    with open(USAGE_FILE, "w") as f:
        f.write(f"{usage['date']},{usage['count']}")

def can_use_api():
    today = str(datetime.today().date())
    usage = load_api_usage()
    if usage["date"] != today:
        usage = {"date": today, "count": 0}
    if usage["count"] < MAX_CALL_PER_DAY:
        usage["count"] += 1
        save_api_usage(usage)
        return True
    return False

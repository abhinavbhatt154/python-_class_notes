# Current date and time in required format
from datetime import datetime
from zoneinfo import ZoneInfo

current_time = datetime.now(ZoneInfo("Asia/Kolkata"))
formatted_time = current_time.strftime("%a %b %d %H:%M:%S IST %Y")

print("Current date and time:", formatted_time)

from datetime import datetime
import pytz

utc = pytz.utc
ist = pytz.timezone('Asia/kolkata')

now = datetime.now(tz=utc)
ist_now = now.astimezone(ist)

print(now)
print(ist_now)

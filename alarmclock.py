from datetime import datetime
from playsound import playsound

hour = input("What hour do you wish to set your alarm for? ")
minute = input("What minute o you wish to set your alarm for?")
alarm = datetime(year=datetime.today().year,
                 month=datetime.today().month, day=datetime.today().day,
                 hour=int(hour), minute=int(minute))
while True:
    if datetime.ctime() == alarm:
        pass

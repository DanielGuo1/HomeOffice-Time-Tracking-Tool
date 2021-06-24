import pandas as pd
from datetime import datetime, timedelta

class WorkingTime():

    # 1 - Beginn Time
    # 2 - Regular Time
    # 3 - Max Time
    def getTime(typ_of_time):
        today = datetime.today()
        df = pd.read_csv(r"StartTime.csv")

        for i in df['TimeWritten']:
            if (today.strftime('%d.%m.%Y') in i):
                shutup_today = i

        datetime_object = datetime.strptime(shutup_today, '%d.%m.%Y %H:%M:%S')

        # Regelarbeitszeit: 8h + 45min Pause
        regularTime = datetime_object + timedelta(hours=8,minutes=45)

        # Regelarbeitszeit: 10h + 45min Pause
        maxTime = datetime_object + timedelta(hours=10, minutes=45)

        if (typ_of_time == 1):
            return datetime_object.strftime('%H:%M:%S')

        elif (typ_of_time == 2):
            return regularTime.strftime('%H:%M:%S')

        elif (typ_of_time == 3):
            return maxTime.strftime('%H:%M:%S')


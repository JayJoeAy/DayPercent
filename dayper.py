from datetime import datetime
import time
def daypercent():
    hr=datetime.now().strftime('%H')
    min=datetime.now().strftime('%M')
    sec=datetime.now().strftime('%S')
    dtime=(int(hr)-6)*3600+int(min)*60+int(sec)
    tot=18*3600
    per=round(((dtime/tot)*100),1)
    print(per)
    time.sleep(60)

while True:
    daypercent()

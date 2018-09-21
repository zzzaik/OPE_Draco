from datetime import datetime

def getDatetimeWithMinDelay(delay=10):
    date = datetime.now().strftime("%Y-%m-%d")
    hour = datetime.now().strftime("%H")
    minute = datetime.now().strftime("%M")
    confMin = int(minute) + delay
    while confMin > 60:
        if confMin == 60:
            hour = int(hour) + 1
            confMin = 00
        if confMin > 60:
            hour = int(hour) + 1
            confMin -= 60
            if confMin < 10:
                confMin = "0%d" %(confMin)
    return '%s %s:%s' %(date, hour, confMin)

def getDateTimeAtual():
    return datetime.now().strftime('%Y-%m-%d %H:%M')

#print(getDateTimeAtual())
#print(getDatetimeWithMinDelay(320))


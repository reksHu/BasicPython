import time

def timePrinter(fn):
    while True:
        timeStr = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        print(timeStr)
        time.sleep(1)
        return fn

def print_service(fn):
    def clock_print(alarmTime):
        while True:
            timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            fn(alarmTime)
            print(timeStr)
            time.sleep(1)
    return clock_print

@print_service
def alarmClock(alarmTime):
    currentTime = time.time()
    print("alarm:",alarmTime,"currentTime:",currentTime)
    if(alarmTime <= currentTime):
        print("Alarming.....")
        exit()

def clock():
    t = time.time()
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(t)))
    afterTime = t+30 #30秒
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(afterTime)))

    # timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t+120))
    # print(timeStr)
    # nt = time.strptime(timeStr,"%Y-%m-%d %H:%M:%S")
    # print(nt)

# timePrinter()

alarmClock(time.time()+60)


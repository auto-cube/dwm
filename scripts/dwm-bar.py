import os
from datetime import datetime
from time import sleep


def cat_comand(path):
    result = os.popen("cat "+path).read()
    return result

def get_battary():
    pathToPowerSupply = "/sys/class/power_supply/"
    pathToBat = pathToPowerSupply+"CMB0/"
    pathToAc = pathToPowerSupply+"ADP1/"
    status =  cat_comand(pathToBat+"status")
    capacity = eval(cat_comand(pathToBat+"capacity"))
    isPlugged =  eval(cat_comand(pathToAc+"online"))


    if status == "Full":
        return "[\uf240 " + str(capacity) + "%]"
    else:
        if isPlugged == 1:
            return "[\uf0e7 " + str(capacity) + "%]"
        else:
            if (capacity>=95)&(capacity<=100):        
                return "[\uf240 " + str(capacity) + "%]"
            elif (capacity>=75)&(capacity<95):
                return "[\uf241  "+ str(capacity)+"%]"
            elif (capacity>=50) &(capacity<75):
                return "[\uf242  "+ str(capacity)+"%]"
            elif (capacity>=25)&(capacity<50):
                return "[\uf243  "+ str(capacity)+"%]"
            else:
                return "[\uf244  "+ str(capacity)+"%]"


def get_light():
    light = eval(os.popen("light -G").read())
    light = int(light)
    return "[\uf0eb "+str(light)+"%]"



def get_volume():
    is_mute = eval((os.popen("pamixer --get-mute")).read().capitalize())
    volume = eval((os.popen("pamixer --get-volume")).read())
    if is_mute ==True:
        return "[\uf026 Mute]"
    else:
        if volume<=30:
            return "[\uf027 "+str(volume)+"%]"
        else:
            return "[\uf028 "+str(volume)+"%]"


def get_datetime():
    time_now = datetime.now().strftime("[\uf017 %Y-%m-%d %a %H:%M:%S]")
    return time_now

def xsetroot_format(func):
    return "'"+func+"'"

while True:
    light = xsetroot_format(get_light())
    battary= xsetroot_format(get_battary())
    volume = xsetroot_format(get_volume())
    time = xsetroot_format(get_datetime())
    os.system("xsetroot -name  "+battary+light+volume+time)
    sleep(1)



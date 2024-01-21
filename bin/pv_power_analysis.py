#!/usr/bin/python3
import sys
import json
import time

start = 0
end   = 0
apogee = 0
top    = 0

query = json.load(sys.stdin)

for i in query:
    t, v = i
    if start == 0:
        if v > 0:
            start = t / 1000
    else:
        if v == 0:
            if end == 0:
                end = t / 1000
        else:
            end = 0
            if v > top:
                apogee = t / 1000
                top = v

print ("Le", time.strftime("%d-%m-%Y",time.gmtime(start)))
print ("debut :", time.strftime("%H:%M",time.gmtime(start)), "GMT")
print ("fin   :", time.strftime("%H:%M",time.gmtime(end)), "GMT")
print ("apogee:", time.strftime("%H:%M",time.gmtime(apogee)), "GMT (", top, "Watts )")
print ()

hstart  = int(time.strftime("%H",time.gmtime(start)))
hend    = int(time.strftime("%H",time.gmtime(end)))
hapogee = int(time.strftime("%H",time.gmtime(apogee)))
mstart  = int(int(time.strftime("%M",time.gmtime(start))) * 100 / 60)
mend    = int(int(time.strftime("%M",time.gmtime(end))) * 100 / 60)
mapogee = int(int(time.strftime("%M",time.gmtime(apogee))) * 100 / 60)
print (str(hstart) + "." + str(mstart), str(hend  ) + "." + str(mend  ), str(hapogee) + "." + str(mapogee), top)

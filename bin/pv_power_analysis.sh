#!/bin/sh
set -e
query=$(/usr/bin/curl -s "http://192.168.42.1/feed/data.json?apikey=86426e02438c2ddede00f695bf54f528&id=108&start=$(date -d 'today 00:00' +%s)000&end=$(date -d 'today 23:59' +%s)000&interval=600"|/usr/bin/python3 $(dirname $0)/pv_power_analysis.py|tail -1)
debut=$(echo $query|cut -d\  -f1)
fin=$(echo $query|cut -d\  -f2)
apogee=$(echo $query|cut -d\  -f3)
top=$(echo $query|cut -d\  -f4)
curl -s \
  --data "node=Inverter&data={pv_power_start:$debut}&apikey=1d87228428ff3f0660954a02860f070e" \
  http://emonpi.local/input/post >/dev/null
curl -s \
  --data "node=Inverter&data={pv_power_end:$fin}&apikey=1d87228428ff3f0660954a02860f070e" \
  http://emonpi.local/input/post >/dev/null
curl -s \
  --data "node=Inverter&data={pv_power_max:$apogee}&apikey=1d87228428ff3f0660954a02860f070e" \
  http://emonpi.local/input/post >/dev/null
curl -s \
  --data "node=Inverter&data={pv_power_top:$top}&apikey=1d87228428ff3f0660954a02860f070e" \
  http://emonpi.local/input/post >/dev/null
exit 0

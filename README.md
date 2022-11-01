# h(e)ms

Home (Energy) Monitoring System

A DIM (do-it-myself) project...

I want an cheap generic IoT edge device with local analytical features.

Come to mind:
- MQTT broker
- logrotate
- influxDB
- mqtt2influxdb
- zigbee2mqtt (smart plugs)
- emonHub (RF2mqtt)
- mqtt-wifi-relay (to pilot the heater)
- 1wire2mqtt (temperare and reeds relays)
- grafana (from influxdb)
- nginx (reverse proxy grafana with encryption and authentication)
- letsencrypt (certs management)
- davis2mqtt (weather station)
- inverter2mqtt (WKS)
- bms2mqtt (pylontech)
- collectd (2influxdb)
- ...

I guess an Alpine Linux running in RUN-FROM-RAM mode will fit the bill as operating system. If not, I will use some debian derivative. \
Will do a first run from a custom APKOVL and as podman's pod, both on x86 hardware. Later on, I will try on Raspberry Pi and other ARM boards (the famous "Armada") I have at the lab...

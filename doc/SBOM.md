In order to run our YAH solution, we are using:

- Operating Sysyem: Alpine Linux
- MQTT broker: mosquitto
- TimeSerie Database: influxDB
- hardware integration: zigbee2mqtt
- dashboards: grafana
- frontend: nginx
- certificate management: certbot (Let's Encrypt)
- key/value store: redis
- scheduler: crond
- metrology: collectd
- agents:
    - z2m2mqtt: format zigbee2mqtt outputs
    - 1-wire2mqtt: poll devices and publish values
    - growatt2mqtt: poll device and publush values
    - weewx2mqtt: module to export directly to MQTT
    - mqtt2mqtt: filter, compute, aggregate, select and publish
    - mqtt2influxdb: inject values in timeseries
    - solarcast2influxdb: inject forecast values in timeserie

Other subsysteasm are not deployed especially for YAH.

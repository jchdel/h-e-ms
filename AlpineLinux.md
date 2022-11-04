# How-to prepare the underlying operating system

see https://alpinelinux.org/

## setup a dev box

I run it as a KVM running with qemu on a Debian stable box. It is an Alpine Linux setup as https://wiki.alpinelinux.org/wiki/Include:Setup_your_system_and_account_for_building_packages

## select wanted packages

We want:
- logrotate; mosquitto; influxdb; grafana; nginx; letsencryt; collectd; 1-wire2mqtt; zigbee2mqtt; weewx2mqtt; inverter's driver2mqtt; modbus2mqtt; wpa-supplicant; bash; 

### services running on baremetal

> /etc/apk/world

### services running in containers

> docker pull ...

## build custom ISO

TBD

## extract local repository and default APKOVL

TBD

## deploy a new node from scratch

TBD

## over-the-air (OTA) update of a running node

TBD

## about A/B boot modes

TBD

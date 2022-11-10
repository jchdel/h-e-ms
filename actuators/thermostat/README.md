In the old farm I rent, the physical thermostat is located above the oven...

I have a Toon running in the kitchen and 4 EmonTh scattered accros the home. All sending their temperature measurements to EmonHub.

A GNU/Linux cronjob fetch values from EmonCMS (API) and follows a decision tree to activate, or deactivate or let in current state, the furnace regarding of the legacy thermostat forced in full heating mode. The cronjob in running on the EmonPi monitoring the home.

The furnace electric power supply is driven by an EmonWifiMqttRelay.

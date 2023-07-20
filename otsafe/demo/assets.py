
from otsafe.components.sensors import Sensor

def get_sensor() -> Sensor:
    tps = Sensor(
        name = "Tank Pressure Sensor",
        description = "Primary pressure sensor attached to top of the vessel",
        id = SENSOR_ID,
        owner = get_owner(SENSOR_ID),
        bu = get_bu(SENSOR_ID),
        type = "Pressure",
        status = "Operational",
        location = "Top of Vessel",
        value = 0,
        units = " PSI",
        min_value = 0,
        max_value = 100,
        min_threshold = 10,
        max_threshold = 90,
        min_alarm = 20,
        min_safety = 15,
        max_alarm = 80,
        max_safety = 85,
        min_alarm_message = "TANK PRESSURE IS DANGEROUSLY LOW!",
        max_alarm_message = "TANK PRESSURE IS DANGEROUSLY HIGH!",
        min_threshold_message = "Tank Pressure is too low!",
        max_threshold_message = "Tank Pressure is too high!"
    )
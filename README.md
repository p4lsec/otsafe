# OTsafe

OTsafe is a Python-based framework which enables new cyber-safety modeling, detection, and response capabilities. Designed to secure critical processes down at the lowest levels, OTsafe allows practitioners to secure systems from cyber-physical threats, where priorities include the protection of people, equipment, and the environment.

## Use Cases

 OTsafe is a tool designed to assist in the following scenarios:

- Highly secured networks, where deviation from baseline should trigger a cybersecurity response. 
- Orgs who have assessed physical risk as a top priority, and want to apply a layer of controls
- Engineers, including cyber risk scenarios while conducting Failure Mode and Effects Analysis (FMEA). 
- OT/IIoT Cybersecurity Engineers, SOCs, and teams who want to ensure that they prioritize the safety of people, equipment, and the environment.  
- CISOs who want to apply an auditable layer of controls to account for cyberattacks or otherwise anomolous observables. 
- People building connectors between disparate data sources, such as historians, inventory management systems, detection, playbooks, thrunting, and more.  
- People who make other software or provide services, whether open or closed source, non- or for-profit.
- People who want to build active and passive asset inventory capabilities. 
- Creative individuals who enjoy making the world a better place, and maybe even want to contribute code to this project. 

Who this is not for:

- Submarine Tycoons
- A helpdesk/IT/network/security team of three people

## Core Library

The core component of OTsafe is a Python library/API, which can be used to represent the pertinent components of a cyber-physical process. Once the components are modeled into a system, the library will allow you to connect your process telemetry data (sensors, valve states, etc) to other processes.  

How to build a sensor in OTsafe:

```
from OTsafe.components.sensors import Sensor

tps = Sensor(
    name = "Tank Pressure Sensor",
    description = "Primary pressure sensor attached to top of the vessel",
    id = "D34DB33F",
    owner = get_owner(id)
    bu = get_bu(id),
    type = "Pressure",
    status = "Operational",
    location = "Top of Vessel",
    value = 20,
    units = " PSI",
    min_value = 0,
    max_value = 100,
    min_threshold = 10,
    max_threshold = 90,
    min_alarm = 0,
    max_alarm = 100,
    min_alarm_delay = 0,
    max_alarm_delay = 0,
    min_alarm_message = "TANK PRESSURE IS DANGEROUSLY LOW!",
    max_alarm_message = "TANK PRESSURE IS DANGEROUSLY HIGH!",
    min_threshold_message = "Tank Pressure is too low!",
    max_threshold_message = "Tank Pressure is too high!",
    min_alarm_enabled = False,
)

# Take live sensor readings. Make your own historian! 
# >>> tps.read()
# 20
# >>>

# Make realistic, noisy sensors.  Build detections based off of noisy baselines! 
# >>> tps.noisy_read(.2)
# 19
# >>> tps.noisy_read(.2)
# 21
# >>> tps.noisy_read(.2)
# 20
# >>>

```

## Detections

Once process telemetry data is successfully ingested, you can build detections for unsafe conditions.  These detections are freeform, and are designed to match the monitored value’s state.  Use cases for detections are wide open to the user!  The best detections will need to be intelligently engineered.  The process engineers and SMEs would need to be involved in building smart detections. 

This will allow them to build detections for anomalous and even malicious modifications to the process. For instance, if a burner was turned on but the PLC did not issue the command, and it's not in a normal state, we could build alerts, or even build automation to override the system and return it to a safe state. Think of it as a layer of safety over the SIS. 

The detection engine relies on a PyModbus server, which applies detections against every packet it's fed.  In the event of a hit, the result can kick off various response processes.  Again, this is left to the creativity of the user!

Included in the `demo/` folder is a tool used to showcase a compromised engineering workstation being used to send malicious commands to a PLC.  The demo also shows how OTsafe can be used to detect the attack, and render the system safe.  

## Automation capabilities

Responding to conditions is the primary responsibility of your OT equipment, as it was originally designed. But in the event that an attacker attempts to compromise a system, an SIS has been targetted, an SIS fails, or otherwise lacks larger context that this system may have, this system can be used to fill risk gaps not otherwise covered. It would be feasible to make cyber "Stop The Job" button, which would take network-wide defensive measures in the event of a disruption (ransomware, malicious attack, unsafe conditions detected, etc)

OTsafe uses Jenkins as the primary orchestration engine.  This allows for easy deployment, plus instant expandability and scalability, while also serving as an automation platform.  

## Disclaimer

- There are so many caveats and unaccounted-for gotchas in this project.  The scope will continue to evolve and change as time marches on.  Please share any feedback you have on this project!  PR and collaboratiors welcome!  

- The use of OTsafe should be viewed as another layer of protection, on top of existing and adequate Safety Instrumented Systems (SIS).  OTsafe is not a life-saving product, and should not be solely relied upon to provide immediate life-saving reliability.  Ubuntu and Python don’t run safety-critical processes.  

## Notes

- This project does NOT use a legitimate physics-based backend.  Attributes do not influence each other, via the use of a physics model or otherwise.  Raising the heat will not have a direct effect on the pressure of a vessel.  Setting the flow rate to 9999999999 will not change any other attributes. 

- Why Python?  First off, let's talk about Python.  It's not the best language!  Pretty much ever, for anything.  But, it is often the second best language.  That may or may not be the case here, who knows.  The Python ecosystem continue to grow and evolve, and new relatives like Mojo aim to solve performance problems in innovative and promising ways, while keeping the familiar native Python syntax.  

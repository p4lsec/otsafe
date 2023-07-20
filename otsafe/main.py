import datetime
import logging
import pyshark

from dotenv import load_dotenv
from os import getenv

from demo.assets import *
from inventory.tasks import get_owner, get_bu


load_dotenv()
log = logging.getLogger(__name__)

SENSOR_ID = "D34DB33F"
VESSEL_ID = "C4FEB4B3"
PUMP_ID = "F00D"
VALVE_ID = "B4D"
BURNER_ID = "B3EF"
ALARM_ID = "5C4R3D"


def main():

    tps = get_sensor()



capture = pyshark.LiveCapture(interface='eth0')
capture.sniff(timeout=50)
capture
<LiveCapture (5 packets)>
>>> capture[3]
<UDP/HTTP Packet>

for packet in capture.sniff_continuously(packet_count=5):
    print('Just arrived:', packet)

if __name__ == '__main__':
    main()
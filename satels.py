from pyorbital.orbital import Orbital
from datetime import datetime, timedelta
import pytz
from pathlib import Path
root = Path()
tle = root / 'tle.txt'
satel_list = ["NOAA 18", "NOAA 19", "METEOR-M2 3", "METEOR-M2 4"]
def choose_satels(satels):
    coors = []
    for i in satels:
        orb = Orbital(i, 'tle.txt')
        now = datetime.now(pytz.utc)
        coors.append([i, orb.get_lonlatalt(now)])
    return coors
from pyorbital.orbital import Orbital
from datetime import datetime, timedelta
import pytz
from pathlib import Path
root = Path()
tle = root / 'tle.txt'
satel_list = ["NOAA 18", "NOAA 19", "METEOR-M2 3", "METEOR-M2 4"]
lon = 37.6156
lat = 55.7522
alt = 0.163

def get_timetable():
    all_passes = []
    for i in satel_list:
        satel_name = i
        orb = Orbital(satel_name, tle_file=str(tle))
        now = datetime.now(pytz.utc)
        one_satel_passes = orb.get_next_passes(now, 24, lon, lat, alt, horizon=20)


        for i in one_satel_passes:
            az, el = orb.get_observer_look(i[2], lon, lat, alt)
            all_passes.append(tuple((satel_name, i[0], i[2], i[1], az, el)))
            #print(satel_name, i[0].strftime('%d.%m.%Y-%H:%M:%S'), i[2].strftime('%d.%m.%Y-%H:%M:%S'), i[1].strftime('%d.%m.%Y-%H:%M:%S'), f"{az:.2f}", f"{el:.2f}", sep='\t')
    all_passes.sort(key=lambda i: i[1])
    return all_passes

        #print(satel_name, i[0].strftime('%d.%m.%Y-%H:%M:%S'), i[2].strftime('%d.%m.%Y-%H:%M:%S'), i[1].strftime('%d.%m.%Y-%H:%M:%S'), f"{az:.2f}", f"{el:.2f}", sep='\t')
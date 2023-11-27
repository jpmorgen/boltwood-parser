from datetime import datetime
from src.boltwood_parser import *


def test_entry():
    entry = WeatherEntry("2018-01-17 14:51:45.00 C M 35.9   78.1  78      0      45  56.1   000 0 0 00020 043117.61927 1 1 1 3 0 0")
    assert entry.time == datetime(2018, 1, 17, 14, 51, 45, 0)
    assert entry.sky_temperature == 35.9
    assert entry.ambient_temperature == 78.1
    assert entry.sensor_temperature == 78
    assert entry.wind_speed == 0
    assert entry.humidity == 45
    assert entry.dew_point == 56.1
    assert entry.dew_heater_percentage == 0
    assert not entry.is_raining
    assert not entry.is_wet
    assert entry.cloudy == CloudyFlags.clear
    assert entry.wind_limit == WindLimitFlags.calm
    assert entry.rain == RainFlags.dry
    assert entry.darkness == DarknessFlags.daylight
    assert not entry.roof_closed
    assert not entry.alert

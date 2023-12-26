from datetime import datetime
from typing import cast

from .flags import *
from .utils import *


class WeatherEntry:
    """
    A class for parsing and storing a single weather entry.
    """

    time: datetime
    """Time at which this entry occured"""
    
    temp_scale: TemperatureType
    """Temperature format"""
    wind_scale: WindSpeedType
    """Wind speed format"""

    sky_temperature: float
    """Sky temperature in specified format"""
    ambient_temperature: float
    """Ambient temperature in specified format"""
    sensor_temperature: float
    """Sensor temperature in specified format"""
    wind_speed: float
    """Wind speed in specified format"""
    humidity: float
    """Humidity"""
    dew_point: float
    """Dewpoint in specified format"""
    dew_heater_percentage: float
    """Dew heater percentage"""

    is_raining: bool
    """Is raining"""
    is_wet: bool
    """Is wet"""

    cloudy: CloudyFlags
    """Cloud status"""
    wind_limit: WindLimitFlags
    """Wind status"""
    rain: RainFlags
    """Rain status"""
    darkness: DarknessFlags
    """Darkness status"""

    roof_closed: bool
    """Is the roof closed"""
    alert: bool
    """Is there an alert"""

    def __init__(self, entry: str):
        """
        Initialize object with a weather entry.

        Parameters
        ----------
        entry : str
            Raw weather entry

        Raises
        ------
        WeatherParseError
            Invalid format
        """

        parsed = entry.split(" ")
        while "" in parsed:
            parsed.remove("")

        self.time = datetime.strptime(
            parsed[0] + " " + parsed[1], "%Y-%m-%d %H:%M:%S.%f")

        self.temp_scale = cast(TemperatureType, parsed[2])
        self.wind_scale = cast(WindSpeedType, parsed[3])

        if self.temp_scale not in ["F", "C"]:
            raise WeatherParseError(f"Invalid temperature scale: {self.temp_scale}")

        if self.wind_scale not in ["M", "K"]:
            raise WeatherParseError(f"Invalid wind speed scale: {self.wind_scale}")

        self.sky_temperature = float(parsed[4])
        self.ambient_temperature = float(parsed[5])
        self.sensor_temperature = float(parsed[6])
        self.wind_speed = float(parsed[7])
        self.humidity = float(parsed[8])
        self.dew_point = float(parsed[9])
        self.dew_heater_percentage = float(parsed[10])

        self.is_raining = int(parsed[11]) == 1
        self.is_wet = int(parsed[12]) == 1

        self.cloudy = CloudyFlags(int(parsed[15]))
        self.wind_limit = WindLimitFlags(int(parsed[16]))
        self.rain = RainFlags(int(parsed[17]))
        self.darkness = DarknessFlags(int(parsed[18]))
        self.roof_closed = int(parsed[19]) == 1
        self.alert = int(parsed[20]) == 1

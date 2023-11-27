from datetime import datetime
from typing import cast
from .flags import *
from .utils import *


class WeatherEntry:
    time: datetime

    sky_temperature: float
    ambient_temperature: float
    sensor_temperature: float
    wind_speed: float
    humidity: float
    dew_point: float
    dew_heater_percentage: float
    
    is_raining: bool
    is_wet: bool

    cloudy: CloudyFlags
    wind_limit: WindLimitFlags
    rain: RainFlags
    darkness: DarknessFlags

    roof_closed: bool
    alert: bool

    def __init__(self, entry: str):
        parsed = entry.split(" ")
        while "" in parsed:
            parsed.remove("")

        self.time = datetime.strptime(parsed[0] + " " + parsed[1], "%Y-%m-%d %H:%M:%S.%f")

        temp_scale = cast(TemperatureType, parsed[2])
        wind_scale = cast(WindSpeedType, parsed[3])
        
        if temp_scale not in ["F", "C"]:
            raise WeatherParseError(f"Invalid temperature scale: {temp_scale}")
        
        if wind_scale not in ["M", "K"]:
            raise WeatherParseError(f"Invalid wind speed scale: {wind_scale}")
        
        self.sky_temperature = processTemp(float(parsed[4]), temp_scale)
        self.ambient_temperature = processTemp(float(parsed[5]), temp_scale)
        self.sensor_temperature = processTemp(float(parsed[6]), temp_scale)
        self.wind_speed = processSpeed(float(parsed[7]), wind_scale)
        self.humidity = processTemp(float(parsed[8]), temp_scale)
        self.dew_point = processTemp(float(parsed[9]), temp_scale)
        self.dew_heater_percentage = float(parsed[10])
        
        self.is_raining = int(parsed[11]) == 1
        self.is_wet = int(parsed[12]) == 1
        
        self.cloudy = CloudyFlags(int(parsed[15]))
        self.wind_limit = WindLimitFlags(int(parsed[16]))
        self.rain = RainFlags(int(parsed[17]))
        self.darkness = DarknessFlags(int(parsed[18]))
        self.roof_closed = int(parsed[19]) == 1
        self.alert = int(parsed[20]) == 1

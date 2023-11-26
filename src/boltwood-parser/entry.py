from datetime import datetime
from .flags import *


class WeatherEntry:
    time: datetime
    sky_temperature: float
    ambient_temperature: float
    sensor_temperature: float
    wind_speed: float
    humidity: int
    dew_point: float
    dew_heater_percentage: int

    cloudy: CloudyFlags
    wind_limit: WindLimitFlags
    rain: RainFlags
    darkness: DarknessFlags

    roof_closed: bool
    alert: bool

    def init(self, entry: str) -> None:
        parsed = entry.split("")
        while "" in parsed:
            parsed.remove("")

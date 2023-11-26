from enum import Enum


class CloudyFlags(Enum):
    clear = 1
    light = 2
    very_cloudy = 3


class WindLimitFlags(Enum):
    calm = 1
    windy = 2
    very_windy = 3


class RainFlags(Enum):
    dry = 1
    damp = 2
    rain = 3


class DarknessFlags(Enum):
    dark = 1
    dim = 2
    daylight = 3

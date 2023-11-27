from typing import Literal


TemperatureType = Literal["F", "C"]
WindSpeedType = Literal["M", "K"]

def FtoC(f: float):
    return (f - 32) * (5/9)

def processTemp(temp: float, format: TemperatureType):
    if (format == "C"):
        return temp
    else:
        return FtoC(temp)
    
def KnotstoMPH(k: float):
    return k * 1.151

def processSpeed(speed: float, format: WindSpeedType):
    if (format == "M"):
        return speed
    else:
        return KnotstoMPH(speed)
    
class WeatherParseError(Exception):
    pass

from typing import Literal


TemperatureType = Literal["F", "C"]
WindSpeedType = Literal["M", "K"]

def FtoC(f: float) -> float:
    """
    Converts Fahrenheit to Celcius.

    Parameters
    ----------
    f : float
        Temperature in Fahrenheit

    Returns
    -------
    float
        Temperature in Celcius
    """
    return (f - 32) * (5/9)


def processTemp(temp: float, format: TemperatureType) -> float:
    """
    Standardized temperature. Converts `temp` to Celcius if `format` is `F`
    and returns `temp` if `format` is `C`

    Parameters
    ----------
    temp : float
        Temperature
    format : TemperatureType
        Boltwood II Format

    Returns
    -------
    float
        Temperature in Celcius
    """
    if (format == "C"):
        return temp
    else:
        return FtoC(temp)
    

def KnotstoMPH(k: float) -> float:
    return k * 1.151


def processSpeed(speed: float, format: WindSpeedType) -> float:
    if (format == "M"):
        return speed
    else:
        return KnotstoMPH(speed)
    
class WeatherParseError(Exception):
    pass

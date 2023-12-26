from typing import Literal

TemperatureType = Literal["F", "C"]
WindSpeedType = Literal["M", "K"]


def f_to_c(f: float) -> float:
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


def c_to_f(c: float) -> float:
    """
    Converts Celcius to Fahrenheit.

    Parameters
    ----------
    c : float
        _description_

    Returns
    -------
    float
        _description_
    """
    return (c * (5/9)) + 32


def process_temp(temp: float, format: TemperatureType) -> float:
    """
    Standardized temperature. Converts `temp` to Celcius if `format` is `F`
    and returns `temp` if `format` is `C`.

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
        return f_to_c(temp)


def knots_to_mph(k: float) -> float:
    """
    Converts knots to MPH.

    Parameters
    ----------
    k : float
        Speed in knots

    Returns
    -------
    float
        Speed in MPH
    """
    return k * 1.151


def mph_to_knots(k: float) -> float:
    """
    Converts MPH to knots.

    Parameters
    ----------
    k : float
        Speed in MPH

    Returns
    -------
    float
        Speed in knots
    """
    return k / 1.151


def process_speed(speed: float, format: WindSpeedType) -> float:
    """
    Standardized speed. Converts `speed` to MPH if `format` is `K`
    and returns `speed` if format is `M`.

    Parameters
    ----------
    speed : float
        Speed
    format : WindSpeedType
        Boltwood II Format

    Returns
    -------
    float
        Speed in MPH
    """
    if (format == "M"):
        return speed
    else:
        return knots_to_mph(speed)


class WeatherParseError(Exception):
    pass

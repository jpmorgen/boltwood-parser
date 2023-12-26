from datetime import datetime
import math
from .entry import WeatherEntry


class EntryCollection:
    """
    A class for parsing, storing, and processing multiple weather entries.
    """

    entries: list[WeatherEntry] = []
    """Entries"""

    def __init__(self, data: str, sort: bool = False) -> None:
        """
        Start parsing through weather entries that are separated by new lines.
        If `sort` is `False`, then the data will not be sorted. In order for
        other processing methods to work, the data must already be in order.

        Parameters
        ----------
        data : str
            Raw weather data. Could be read from a file.
        sort : bool, optional
            Sort the data by time, by default `False`
        """
        lines = data.splitlines()
        for i in lines:
            if i.strip() == "":
                continue
            self.entries.append(self.process_entry(i))

        if sort:
            self.entries.sort(key=lambda x: x.time.timestamp())

    def process_entry(self, line: str) -> WeatherEntry:
        """
        Process and entry before storing it. Override this to use custom
        weather entry objects.

        Parameters
        ----------
        line : str
            Raw entry

        Returns
        -------
        WeatherEntry
            Processed entry
        """
        return WeatherEntry(line)
    
    def find(self, time: datetime) -> WeatherEntry:
        """
        Finds the next weather entry after this time.

        Parameters
        ----------
        time : datetime
            Time

        Returns
        -------
        WeatherEntry
            Weather entry after `time`
        """
        return self.__find(time)
        
        
    def __find(self, time: datetime, _low: int = 0, _high: int = -1) -> WeatherEntry:
        """
        Internal method for searching
        """
        if _high == -1:
            _high = len(self.entries) - 1
            
        if _high == _low:
            return self.entries[_high]
        
        mid = math.floor(_low + ((_high - _low) / 2))
        if self.entries[mid].time > time:
            return self.__find(time, _low, mid)
        else:
            return self.__find(time, mid + 1, _high)

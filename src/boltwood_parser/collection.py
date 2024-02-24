from datetime import datetime
import math
from typing import cast
from .entry import WeatherEntry


class EntryCollection:
    """
    A class for parsing, storing, and processing multiple weather entries.
    """

    entries: list[WeatherEntry | str] = []
    """Entries"""

    def __init__(self, data: str, preprocess: bool = False, sort: bool = False) -> None:
        """
        Start parsing through weather entries that are separated by new lines.
        If `sort` is `False`, then the data will not be sorted. In order for
        other processing methods to work, the data must already be in order.

        Parameters
        ----------
        data : str
            Raw weather data. Could be read from a file
        preprocess : bool, optional
            Preprocesses weather data, by default `False`
        sort : bool, optional
            Sort the data by time, by default `False`. Sets `preprocess` to `True`.
        """
        if sort: preprocess = True
        
        lines = data.splitlines()
        
        if preprocess:
            for i in lines:
                if i.strip() == "":
                    continue
                try:
                    self.entries.append(self.process_entry(i))
                except Exception as e:
                    print(f"ERROR: received {e} when parsing {i}")
        else:
            self.entries = cast(list[WeatherEntry | str], lines)

        if sort:
            def predicate(x: WeatherEntry | str):
                if type(x) is WeatherEntry:
                    return x.time.timestamp()
                else:
                    return 0
            
            self.entries.sort(key=predicate)

    def process_entry(self, line: str) -> WeatherEntry:
        """
        Process an entry before storing it. Override this to use custom
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
    
    def parse(self, index: int) -> WeatherEntry:
        """
        Parse a line and return the entry, or return the entry if already parsed.

        Parameters
        ----------
        index : int
            Index

        Returns
        -------
        WeatherEntry
            Entry
        """
        entry = self.entries[index]
        if type(entry) is str:
            processed = self.process_entry(entry)
            self.entries[index] = processed
            return processed
        elif type(entry) is WeatherEntry:
            return entry
        else:
            raise TypeError(f"Entry {entry} is neither a string nor a WeatherEntry.")
    
    def find(self, time: datetime) -> WeatherEntry:
        """
        Finds the closest weather entry to this time.

        Parameters
        ----------
        time : datetime
            Time

        Returns
        -------
        WeatherEntry
            Weather entry closest to `time`
        """
        if time < self.parse(0).time:
            return self.parse(0)
        elif time > self.parse(-1).time:
            return self.parse(-1)
        
        return self._find(time)
        
    def _find(self, time: datetime, _low: int = 0, _high: int = -1) -> WeatherEntry:
        """
        Internal method for searching. Does not account for first or last entry.
        """
        if _high == -1:
            _high = len(self.entries) - 1
            
        if _high == _low:
            found = self.parse(_high)
            next_to_found = self.parse(_high - 1)
            if abs(time.timestamp() - found.time.timestamp()) < abs(time.timestamp() - next_to_found.time.timestamp()):
                return found
            else:
                return next_to_found
        
        mid = math.floor(_low + ((_high - _low) / 2))
        if self.parse(mid).time > time:
            return self._find(time, _low, mid)
        else:
            return self._find(time, mid + 1, _high)

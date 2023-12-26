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

from dataclasses import dataclass


@dataclass
class Aereoporti():
    ID: int
    IATA_CODE :str
    AIRPORT :str
    CITY: str
    STATE: str
    COUNTRY : str
    LATITUDE: float
    LONGITUDE: float
    TIMEZONE_OFFSET: float
    def __str__(self):
        return f"L'aereoporto {self.ID} è conosciuto con il nome di {self.AIRPORT}"

    def __eq__(self, other):
        return self.ID == other.ID

    def __hash__(self):
        return hash(self.ID)


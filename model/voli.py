import datetime
from dataclasses import dataclass


@dataclass
class Voli():
    ID : int
    AIRLINE_ID: int
    FLIGHT_NUMBER:int
    TAIL_NUMBER:str
    ORIGIN_AIRPORT_ID:int
    DESTINATION_AIRPORT_ID:int
    SCHEDULED_DEPARTURE_DATE: datetime.datetime
    DEPARTURE_DELAY: float
    ELAPSED_TIME:float
    DISTANCE:int
    ARRIVAL_DATE:datetime.datetime
    ARRIVAL_DELAY:float

    def __eq__(self, other):
        return self.ID == other.ID
    def __str__(self):
        return f"ID: {self}, aereoporto di partenza {self.ORIGIN_AIRPORT_ID} e quello di arrivo: {self.DESTINATION_AIRPORT_ID}"
    def __hash__(self):
        return hash(self.ID)
import pandas as pd
from utils.table import Table
import random 

class Openspace:
    def __init__(self, capacity : int, n_of_seat):
        self.capacity = capacity
        self.tables = [Table(n_of_seat) for _ in range(self.capacity)]


    def organize(self, names : list [str]) -> None:
        '''asign seat for each person
        args name : str'''
        
        random.shuffle(names)
        
        for table in self.tables:
            for seat in table.seats:
                seat.set_occupant(names[0])
                names.pop(0)


    def display(self):
        for i, table in enumerate(self.tables, start=1):
            occupants: str = ", ".join([seat.occupant for seat in table.seats if not seat.free])
            print(f"Table {i} : {occupants}")
            
    
    def store(self) -> None:
        """
        Save the tables configuration in an excel file
        """

        list_of_tables: list[list[str]] = []
        for table in self.tables:
            list_of_seats: list[str] = []
            for seat in table.seats:
                list_of_seats.append(seat.occupant)
            list_of_tables.append(list_of_seats)

        df = pd.DataFrame(list_of_tables)
        df.to_excel("tables.xlsx", index=False)
        



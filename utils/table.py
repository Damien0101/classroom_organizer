class Seat:
    def __init__(self):
        self.free = True
        self.occupant = None

    
    def set_occupant(self, name : str) -> None:
        '''assign a seat to a person if it's free
        args : name of the persone to assign'''
        
        if self.free:
            self.occupant = name
            self.free = False

    
    def remove_occupant(self) -> str | None:
        '''remove person from a seat'''
        
        if not self.free:
            occupant_name = self.occupant
            self.occupant = None
            self.free = True
            print(f"{occupant_name} removed from this seat")
            return occupant_name
        

class Table:
    def __init__(self, capacity : int = 4):
        self.capacity = capacity
        self.seats : list [Seat] = [Seat() for _ in range(capacity)]


    def has_free_spot(self) -> bool : 
        '''check for at least a free seat'''
        
        for seat in self.seats:
            if seat.free:
                return True
        return False


    def assign_seat(self, name : str) -> None:
        '''assign a person to a seat
        args name : str = name of person'''
        
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
        print("there is no available seat")


    def left_capacity(self) -> int:
        '''check how many free seat are available'''
        
        free_seats= sum(1 for seat in self.seats if seat.free)
        return free_seats


class Computer:

    # What attributes will it need?
    description: str = ""
    processor_type: str = ""
    hard_drive_capacity: int = 0
    memory: int = 0
    operating_system: str = ""
    year_made: int = 0
    price: int = 0
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, 
                 memory: int, operating_system: str, year_made: int, price:int) -> None:
        self.description = description;
        self.processor_type = processor_type;
        self.hard_drive_capacity: hard_drive_capacity;
        self.memory = memory;
        self.operating_system = operating_system;
        self.year_made = year_made;
        self.price = price;
    # What methods will you need?

    #update the price of a computer
    def update_price(self, new_price: int):
        self.price = new_price;
    
    #update the computer OS
    def update_OS(self, new_OS: str):
        self.operating_system = new_OS;

    #reassign the price value to a computer based on age, and update the os system
    def refurbish(self, new_os:[str] = None):
        if self.year_made < 2000:
              self.price = 0     
        elif self.year_made < 2012:
            self.price = 250
        elif self.year_made < 2018:
                self.price = 550
        else:
            self.price = 1000
        if new_os is not None:
             # if os does not equal new_os, update os
            self.operating_system = new_os

    #return all of the attributes of a computer so it can be printed in desired formatting
    def return_attributes(self):
         return ("{'description': '" + self.description +  "', 'processor-type': '" + self.processor_type 
                 + "', 'hard_drive_capacity': " + str(self.hard_drive_capacity) + ", 'memory': " 
                 + str(self.memory) +  ", 'opterating_system': '" + self.operating_system 
                 + "', 'year_made': " + str(self.year_made) + ", 'price': " + str(self.price) + "}")
         

def main():
        firstComputer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5", 1024, 64,
        "macOS Big Sur", 2013, 1500)
        print(firstComputer)
        print(firstComputer.description)
        print(firstComputer.price)
        new_OS = "MacOS Monterey"
        firstComputer.refurbish(new_OS)
        print(firstComputer.price)
        print(firstComputer.return_attributes())

if __name__ == "__main__" :
     main()

#create a method to print 
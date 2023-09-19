from computer import * #import computer class

class ResaleShop:

    # What attributes will it need?
    inventory = []; # create an inventory to store computers
    itemID: int;

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, initialID: int):
        self.inventory = []; # I'm not sure if this is the correct was to set up the inventory...
        self.itemID = initialID;
    
    # What methods will you need?

    # buy a computer, add to inventory
    def buy(self, computer: Computer):
        #add computer to inventory by appending the array
        self.inventory.insert(self.itemID, computer)
        # increment itemID for the next time a computer is bought
        self.itemID += 1
        return self.itemID
    
    # sell a computer, remove from inventory
    def sell(self, itemID: int): #doesn't work properly yet
        # what this should be: if there is something existing in the array at index itemID...
        if itemID - 1 < len(self.inventory): 
            # make it tell you that the computer description was sold
            print(self.inventory[itemID - 1].description + " sold!")
            del self.inventory[itemID - 1]
            self.itemID -= 1
        else:
            print(self.inventory[itemID-1].description, " not found. Please select another item to sell.")
    
    # print the inventory of computers
    def print_inventory(self):
        if self.inventory:
            # print all attributes for each computer in the inventory
            for i in range (0, self.itemID):
                print("Item ID: " + str(i + 1) + ": " + self.inventory[i].return_attributes())
        else:
            print("No inventory to display.")
    

def main():
   """ # create a resale computer shop!
    computerShop = ResaleShop(0)
    # create a computer
    computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5", 1024, 64,
        "macOS Big Sur", 2013, 1500)
    computer1 = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E2000", 1024, 64,
        "macOS Big Sur", 2013, 1500)
    print(computer.description)
    print(computer.price)
    computerShop.buy(computer)
    computerShop.sell(7) #does not work yet
    computerShop.buy(computer1)
    #print(computerShop.inventory[0].price)
    #print(computerShop.inventory[1].return_attributes())
    computerShop.print_inventory() # can print inventory
    computerShop.sell(0) #how can we sell multiple things if the computer_ID will change every time?
    computerShop.sell(0) #shouldn't be able to do this...but index place changes when the first value was deleted
    computerShop.print_inventory()
    computerShop.sell(1)
    computerShop.print_inventory()
    computerShop.sell(4) # sell method is working, but not when checking to see if something isn't there """

# Make a shop to sell from
computerShop = ResaleShop(0)

# First, let's make a computer 
computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5", 1024, 64,
        "macOS Big Sur", 2013, 1500)

# Print a little banner
print("-" * 21)
print("COMPUTER RESALE STORE")
print("-" * 21)

# Add it to the resale store's inventory
print("Buying", computer.description)
print("Adding to inventory...")
computer_id = computerShop.buy(computer)
print("Done.\n")

# Make sure it worked by checking inventory
print("Checking inventory...")
computerShop.print_inventory()
print("Done.\n")

# Now, let's refurbish it
new_OS = "MacOS Monterey"
print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
print("Updating inventory...")
computerShop.inventory[computer_id - 1].refurbish(new_OS)
print("Done.\n")

# Make sure it worked by checking inventory
print("Checking inventory...")
computerShop.print_inventory()
print("Done.\n")

# Now, let's sell it!
print("Selling Item ID:", computer_id)
computerShop.sell(computer_id)

# Make sure it worked by checking inventory
print("Checking inventory...")
computerShop.print_inventory()
print("Done.\n")
    
if __name__ == "__main__" :
     main()
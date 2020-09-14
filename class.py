class flight():

    def __init__(self,capacity):
        self.capacity=capacity
        self.passengers=[]
    
    def openseat(self):
        return self.capacity - len(self.passengers)
    
    def addpassenger(self,name):
        if not self.openseat():
            return False
        self.passengers.append(name)
        return True
    

Flight=flight(3)
 
passengers=["clarke","bellamy","octavia","murphy"]

for person in passengers:
    success=Flight.addpassenger(person)
    if success:
        print(f"Added {person} to the flight successfully")
    else:
        print(f"Failed to add {person} to the flight!!")
   
    


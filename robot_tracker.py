
class Robot:
    def __init__(self,name):
        self.coords = {"x" :0, "y":0, "d":0}
        print(name,"is online")
        self.name = name
        self.help()

    def __str__(self):
        return f"{self.name}"

    def __call__(self):
        while 1:
            command = input (f"Please give a command to {self.name} > ")
            if command == "Q":
                break
            if command == "turn_left":
                self.coords["d"] = (self.coords["d"]-1)% 4
            if command == "turn_right":
                self.coords["d"] = (self.coords["d"]+1)% 4
            if command == "move":            
                if self.coords["d"] == 0:
                    self.coords["y"] += 1
                if self.coords["d"] == 2:
                    self.coords["y"] -= 1
                if self.coords["d"] == 1:
                    self.coords["x"] += 1
                if self.coords["d"] == 3:
                    self.coords["x"] -= 1
            print(self.coords)        
    
    def __del__(self):
        print(self.name,"is offline")
    
    def help(self):
        print("""

        Valid commands are:
        turn_left
        turn_right
        move
        Q
        
        """)

curiosity = Robot("Curiosity")

curiosity()



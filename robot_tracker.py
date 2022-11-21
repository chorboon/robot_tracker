
class Robot:
    def __init__(self):
        self.coords = {"x" :0, "y":0, "d":0}
        print("Robot is online")

    def __call__(self,command):
        if command == "turn_left":
            self.coords["d"] = (self.coords["d"]-1)% 4
        if command == "turn_right":
            self.coords["d"] = (self.coords["d"]+1)% 4
        if command == "move":            
            if self.coords["d"] == 0:
                self.coords["y"] += 1
            if self.coords["d"] == 1:
                self.coords["y"] -= 1
            if self.coords["d"] == 2:
                self.coords["x"] += 1
            if self.coords["d"] == 3:
                self.coords["x"] -= 1
    
    def __del__(self):
        print("Robot is offline")
            

curiosity = Robot()

curiosity("turn_left")

curiosity("move")

curiosity("turn_right")

curiosity("move")
curiosity("move")
curiosity("move")
curiosity("turn_right")
curiosity("move")

curiosity.__del__()
print(curiosity.coords)
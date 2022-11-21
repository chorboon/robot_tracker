
class Robot:
    def __init__(self):
        self.coords = {"x" :0, "y":0, "d":0}
        print("Robot is online")
        self.help()

    def __call__(self,command):
        if command == "Q":
            exit()
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
    
    def __del__(self):
        print("Robot is offline")
    
    def help(self):
        print("""Valid commands are:
        turn_left
        turn_right
        move
        Q
        
        """)

curiosity = Robot()

while 1:
    command_input = input ("Please give a command to curiousity > ")
    curiosity(command_input)
    print(curiosity.coords)

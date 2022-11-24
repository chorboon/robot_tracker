
class Robot:
    def __init__(self,name):
        self.coords = {"x" :0, "y":0, "d":0}
        print(name,"is online")
        self.name = name
        self.command_dict = {"Q"    : "Shutdown", 
                             "tl"   : "Turn left",
                             "tr"   : "Turn right",
                             "move" : "Move"
        }

        self.help()

    def __str__(self):
        return f"{self.name}"

    def __call__(self):
        while 1:
            command = input (f"Please give a command to {self.name} > ")
            if command == "Q":
                break
            if command == "tl":
                self.coords["d"] = (self.coords["d"]-1)% 4
            if command == "tr":
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
        print(f"Valid commands are: {self.command_dict}        ")

curiosity = Robot("Curiosity")

curiosity()



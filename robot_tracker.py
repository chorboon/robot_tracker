
class Robot:
     """
     """
     def __init__(self):
          self._direction = 0
          self._location = [0,0]
          print("Robot online")
          self.display_help()

     def display_help(self):
          print("North South East West Move ? Q")

     def direction(self):
          return self._direction
         

     def location(self):
          return self._location


     def op(self,command):
         print(command)
         if command == "":
             print(direction_dict[self.direction()])
             print(self.location())
             self.display_help()
         elif command in ("L","R","l","r"):
             self.turn(command)
         elif command in("M","m"):
             self.move()
         elif command in ("?"):
             self.display_help()
         elif command in ("Q","q"):
             print("Robot shutting down")
             return False
         else:
             print("Invalid command")
             self.display_help()
         return True

     def move(self):
          if direction_dict[self._direction] == "North":
              self._location[1] += 1
          if direction_dict[self._direction] == "South":
              self._location[1] -= 1
          if direction_dict[self._direction] == "East":
              self._location[0] += 1
          if direction_dict[self._direction] == "West":
              self._location[0] -= 1
          print(direction_dict[self.direction()])
          print(self.location())
          return

     def turn(self,turn):
          if turn == "L":
              self._direction = (self._direction - 1) % 4
          if turn == "R":
              self._direction = (self._direction + 1) % 4
          print(direction_dict[self.direction()])
          print(self.location())
          return


def main():

        r = Robot()

        global direction_dict

        robot_is_online = True
        direction_dict = {0:"North",1:"East",2:"South",3:"West"}

        print(direction_dict[r.direction()])
        print(r.location())
        print(direction_dict[r.direction()])
        print(r.location())
        while robot_is_online:
            robot_is_online = r.op(input("> "))


main()

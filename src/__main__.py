from src.dungeon.grid import Grid
from src.rooms.room import Room

r1 = Room(room_name= '1', 
          x=1, 
          y=2, 
          east_door=(True,None),
          north_door=(True,'x'))

r2 = Room(room_name= '2', 
          x=2, 
          y=2, 
          west_door=(True,None),
          south_door=(True,None))

r3 = Room(room_name= '3', 
          x=1, 
          y=1, 
          west_door=(True,None),
          south_door=(True,None),
          north_door=(True,None),
          east_door=(True,None))

r4 = Room(room_name= '4', 
          x=0, 
          y=1, 
          south_door=(True,None),
          east_door=(True,None))


r5 = Room(room_name= '5', 
          x=0, 
          y=0, 
          south_door=(True,None),
          north_door=(True,None))

r6 = Room(room_name= '6', 
          x=2, 
          y=1, 
          east_door=(True,None),
          west_door=(True,None))

rooms = [r1,r2,r3,r4,r5,r6]

g = Grid(rooms)

while True:
    g.draw_grid()
    action = input("Action: ")

    if action == "g":
        dir = input("Gravity magic direction: ")
        g.apply_gravity(dir)

    if action == 's':
        g.shuffle()
    
    if action == 'm':
        selected_room = input("select room (format: x y): ")
        coords = selected_room.split()
        x, y = int(coords[0]), int(coords[1])

        dir = input("Room movement direction: ")
        g.move_room(dir,x,y)



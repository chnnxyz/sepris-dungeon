from src.dungeon.grid import Grid
from src.rooms.room import Room
from src.rooms.control_rooms import GravityRoom, PanelRoom, EmptySpace

r1 = Room(room_name= '1', 
          x=1, 
          y=2, 
          south_door=(True,None),
          north_door=(True,None),
          spawn_chance=0.25)

r2 = PanelRoom(room_name= '2', 
          x=2, 
          y=2, 
          west_door=(True,None),
          north_door=(True,None),
          spawn_chance=0.25)

r7 = Room(room_name= '2', 
          x=0, 
          y=2, 
          west_door=(True,None),
          north_door=(True,None),
          south_door=(True,None),
          spawn_chance=0.33)

r3 = GravityRoom(room_name= '3', 
          x=1, 
          y=1, 
          west_door=(True,None),
          south_door=(True,None),
          north_door=(True,None),
          east_door=(True,None),
          spawn_chance=0.5)

r4 = Room(room_name= '4', 
          x=0, 
          y=1, 
          south_door=(True,None),
          east_door=(True,None),
          north_door=(True, None),
          spawn_chance=0.33)


r5 = Room(room_name= '5', 
          x=0, 
          y=0, 
          south_door=(True,None),
          north_door=(True,None),
          east_door=(True, None),
          spawn_chance=0.33)

r6 = Room(room_name= '6', 
          x=1, 
          y=0, 
          north_door=(True,None),
          west_door=(True,None),
          spawn_chance=0.25)


rooms = [r1,r2,r3,r4,r5,r6,r7]

g = Grid(rooms)

while True:
    for i in range(len(g.base_grid)):
        for j in range(len(g.base_grid[i])):
            if g.base_grid[i][j].party==True:
                print(f'party is at x={j}, y={i}')
    g.draw_grid()

    for i in range(len(g.base_grid)):
        for j in range(len(g.base_grid[i])):
            if g.base_grid[i][j].party:

                if isinstance(g.base_grid[i][j], GravityRoom):
                    print('Party is at a gravity room')
                elif isinstance(g.base_grid[i][j],PanelRoom):
                    print('Party is at a panel room')
                elif isinstance(g.base_grid[i][j], EmptySpace):
                    print('Party really really shouldnt be here')
                else:
                    print('Party is at a normal room')

                print(f'items: {g.base_grid[i][j].items}')
                print('\n')
    
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
    
    if action == 'e':
        door = input('select door to enter: ')
        g.move_party(door)

    if action == 'fp':
        for i in range(len(g.base_grid)):
            for j in range(len(g.base_grid[i])):
                if g.base_grid[i][j].party==True:
                    print(f'party is at x={g.base_grid[i][j].x}, y={g.base_grid[i][j].y}')



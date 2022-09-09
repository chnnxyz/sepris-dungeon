from typing import List, Tuple
import random
from src.rooms.room import Room
from src.rooms.control_rooms import EmptySpace

class Grid:
    def __init__(self, 
                 rooms: List[Room],
                 entrance: Tuple[int,int,str] = (2,1,'s'),
                 exit:Tuple[int,int,str] = (0,1,'n')) -> None:
        # Initialize empty grid
        self.base_grid = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        
        self.entrance = entrance
        self.exit = exit
       
        # Fill rooms
        for room in rooms:
            # Control for cases where x or y may get repeated
            if self.base_grid[room.y][room.x] is None:
                self.base_grid[room.y][room.x] = room
            else:
                for row in self.base_grid:
                    try:
                        emptycol = self.base_grid[row].index(None)
                        self.base_grid[row,emptycol] = room
                    except:
                        continue
        
        for i in range(len(self.base_grid)):
            for j in range(len(self.base_grid[i])):
                if self.base_grid[i][j] is None:
                    self.base_grid[i][j] = EmptySpace('empty',x=j,y=i)

        # Add party to room
        for i in range(len(self.base_grid)):
            for j in range(len(self.base_grid[i])):
                if j == entrance[0] and i == entrance[1]:
                    self.base_grid[j][i].enter()
    
    def apply_gravity(self, direction:str) -> None:
        '''
        Shifts all rooms in a particular direction, considering collision

        Arguments
        -----------
        - direction [str]: 'n', 's', 'e', or 'w', direction to move the full
                           map to
        '''
        if direction=='w':
            for i in range(len(self.base_grid)):
                self.base_grid[i] = sorted(self.base_grid[i], key=lambda x: isinstance(x,EmptySpace))

        if direction=='e':
            for i in range(len(self.base_grid)):
                self.base_grid[i] = sorted(self.base_grid[i], key=lambda x: not isinstance(x,EmptySpace))

        # North   
        if direction == 'n':
            #transpose shit
            transposed = [list(x) for x in zip(*self.base_grid)]
            for i in range(len(transposed)):
                transposed[i] = sorted(transposed[i], key=lambda x: isinstance(x,EmptySpace))
            
            self.base_grid = [list(x) for x in zip(*transposed)]

        #south
        if direction == 's':
            #transpose shit
            transposed = [list(x) for x in zip(*self.base_grid)]
            for i in range(len(transposed)):
                transposed[i] = sorted(transposed[i], key=lambda x: not isinstance(x,EmptySpace))
            
            self.base_grid = [list(x) for x in zip(*transposed)]

        for i in range(len(self.base_grid)):
            for j in range(len(self.base_grid[i])):
                self.base_grid[i][j].update_position(x=j, y=i)
            
    def move_room(self, direction:str, x:int, y:int) -> None:
        '''
        Moves a single room

        Arguments
        -----------
        - direction [str]: 'n','s','e', or 'w'. Direction to move the room to
        - x [int]: room x position
        - y [int]: room y position
        '''
        selected_room = self.base_grid[y][x]

        if direction == 'n':
            if selected_room.y == 0:
                pass
            elif not isinstance(self.base_grid[y-1][x], EmptySpace):
                pass
            else:
                self.base_grid[y-1][x], self.base_grid[y][x] = self.base_grid[y][x], self.base_grid[y-1][x]
            
        if direction == 's':
            if selected_room.y == 2:
                pass
            elif not isinstance(self.base_grid[y+1][x], EmptySpace):
                pass
            else:
                self.base_grid[y+1][x], self.base_grid[y][x] = self.base_grid[y][x], self.base_grid[y+1][x]

        if direction == 'w':
            if selected_room.x == 0:
                pass
            elif not isinstance(self.base_grid[y][x-1], EmptySpace):
                pass
            else:
                self.base_grid[y][x-1], self.base_grid[y][x] = self.base_grid[y][x], self.base_grid[y][x-1]

        if direction == 'e':
            if selected_room.x == 2:
                pass
            elif not isinstance(self.base_grid[y][x+1], EmptySpace):
                pass
            else:
                self.base_grid[y][x+1], self.base_grid[y][x] = self.base_grid[y][x], self.base_grid[y][x+1]
            
        for i in range(len(self.base_grid)):
            for j in range(len(self.base_grid[i])):
                self.base_grid[i][j].update_position(x=j, y=i)
            
    def move_party(self, direction:str) -> None:
        curr_spot = (999,999)
        for i in range(len(self.base_grid)):
            for j in range(len(self.base_grid[i])):
                if self.base_grid[i][j].party:
                    curr_spot = (j, i)

        if direction == 'w':
            if curr_spot[0] == 0:
                pass
            else:
                self.base_grid[curr_spot[1]][curr_spot[0]].exit()
                self.base_grid[curr_spot[1]][curr_spot[0]-1].enter()

        if direction == 'e':
            if curr_spot[0] == 2:
                pass
            else:
                self.base_grid[curr_spot[1]][curr_spot[0]].exit()
                self.base_grid[curr_spot[1]][curr_spot[0]+1].enter()

        if direction == 's':
            if curr_spot[1] == 2:
                pass
            else:
                self.base_grid[curr_spot[1]][curr_spot[0]].exit()
                self.base_grid[curr_spot[1]+1][curr_spot[0]].enter()

        if direction == 'n':
            if curr_spot[1] == 0:
                pass
            else:
                self.base_grid[curr_spot[1]][curr_spot[0]].exit()
                self.base_grid[curr_spot[1]-1][curr_spot[0]].enter()

        

    def shuffle(self) -> None:
        '''
        Shuffles all dungeon rooms through apply_gravity()
        '''
        choices = ['n','s','e','w']
        for _ in range(20):
            dir = random.choice(choices)
            self.apply_gravity(dir)

    def draw_room(self,room:Room,g:str) -> str:
        '''
        draws all elements of a single room

        Arguments
        -----------
        - room [Room]: Room object
        - g [str]: Base Grid

        Returns
        -----------
        - [str]: drawn grid
        '''

        lines = g.split("\n")
        if isinstance(room, EmptySpace):
            for i in range(3):
                lines[(4*room.y)+i+1] = (lines[(4*room.y)+i+1][:10*room.x +1] + 
                                     "#"*9 +
                                     lines[(4*room.y)+i+1][10*(room.x +1):])
            
        else:
            #Draw North
            if room.doors['north'][0] == True:
                if room.doors['north'][1] is None:
                    lines[(4*room.y)+1] = (lines[(4*room.y)+1][:10*room.x +1] +
                                            "   ---   " +
                                        lines[(4*room.y)+1][10*(room.x +1):])
                else:
                    lines[(4*room.y)+1] = (lines[(4*room.y)+1][:10*room.x +1] +
                                            f"   {room.doors['north'][1]*3}   " +
                                        lines[(4*room.y)+1][10*(room.x +1):])
            
            # Draw South
            if room.doors['south'][0] == True:
                if room.doors['south'][1] is None:
                    lines[(4*(room.y+1))-1] = (lines[(4*(room.y+1))-1][:10*room.x +1] +
                                            "   ---   " +
                                        lines[(4*(room.y+1))-1][10*(room.x +1):])
                else:
                    lines[(4*(room.y+1))-1] = (lines[(4*(room.y+1))-1][:10*room.x +1] +
                                            f"   {room.doors['south'][1]*3}   " +
                                        lines[(4*(room.y+1))-1][10*(room.x +1):])

            # Draw West
            if room.doors['west'][0] == True:
                if room.doors['west'][1] is None:
                    lines[(4*room.y)+2] = (lines[(4*room.y)+2][:10*room.x +1] +
                                            " |" +
                                        lines[(4*room.y)+2][10*(room.x +1)-7:])
                else:
                    lines[(4*room.y)+2] = (lines[(4*room.y)+2][:10*room.x +1] +
                                        f" {room.doors['west'][1]}" +
                                        lines[(4*room.y)+2][10*(room.x +1)-7:])

            # Draw east
            if room.doors['east'][0] == True:
                if room.doors['east'][1] is None:
                    lines[(4*room.y)+2] = (lines[(4*room.y)+2][:10*room.x +1+7] +
                                            "| " +
                                        lines[(4*room.y)+2][10*(room.x +1):])
                else:
                    lines[(4*room.y)+2] = (lines[(4*room.y)+2][:10*room.x +1+7] +
                                        f"{room.doors['east'][1]} " +
                                        lines[(4*room.y)+2][10*(room.x +1):])

        # Draw party
        if room.party:
            lines[(4*room.y)+2] = (lines[(4*room.y)+2][:10*room.x +1+4] +
                                    "P" +
                                    lines[(4*room.y)+2][10*(room.x +1)-4:]
                                )
            
        out = '\n'.join(lines)
        return out
    
    def get_grid(self):
        return self.base_grid

    def draw_grid(self):
        base_drawing = '''
+---------+---------+---------+
|         |         |         |
|         |         |         |
|         |         |         | 
+---------+---------+---------+
|         |         |         |
|         |         |         |
|         |         |         | 
+---------+---------+---------+
|         |         |         |
|         |         |         |
|         |         |         | 
+---------+---------+---------+
'''
        #janky fix
        base_drawing = base_drawing.split('\n')
        base_drawing = base_drawing[1:]
        base_drawing = "\n".join(base_drawing)
        bg = self.get_grid()
        for i in range(len(bg)):
            for j in range(len(bg[i])):
                base_drawing = self.draw_room(bg[i][j], 
                                              base_drawing)

        print(base_drawing)

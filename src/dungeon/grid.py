from typing import List, Tuple
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


    def _check_colission(self):
        pass
    
    def apply_gravity(self, direction:str):
        if direction=='w':
            for i in range(len(self.base_grid)):
                self.base_grid[i] = sorted(self.base_grid[i], key=lambda x: isinstance(x,EmptySpace))
                for j in range(len(self.base_grid[i])):
                    self.base_grid[i][j].update_position(x=j, y=i)

        if direction=='e':
            for i in range(len(self.base_grid)):
                self.base_grid[i] = sorted(self.base_grid[i], key=lambda x: not isinstance(x,EmptySpace))
                for j in range(len(self.base_grid[i])):
                    self.base_grid[i][j].update_position(x=j, y=i)

        # North   
        if direction == 'n':
            #transpose shit
            transposed = [list(x) for x in zip(*self.base_grid)]
            for i in range(len(transposed)):
                transposed[i] = sorted(transposed[i], key=lambda x: isinstance(x,EmptySpace))
            
            self.base_grid = [list(x) for x in zip(*transposed)]
            for i in range(len(self.base_grid)):
                for j in range(len(self.base_grid[i])):
                    self.base_grid[i][j].update_position(x=j, y=i)

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
            
            
        

    def move_room(self, direction:str, x:int, y:int):
        pass

    def draw_room(self,room:Room,g:str):
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

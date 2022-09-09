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
            if self.base_grid[room.x][room.y] is None:
                self.base_grid[room.x][room.y] = room
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
                    self.base_grid[i][j] = EmptySpace('empty',x=i,y=j)


    def _check_colission(self):
        pass
    
    def shift_grid(self, direction:str):
        pass

    def move_room(self, direction:str, x:int, y:int):
        pass

    def draw_room(self,room:Room,g:str):
        lines = g.split("\n")
        if isinstance(room,EmptySpace):
            for i in range(3):
                lines[(4*room.y)+i+1] = (lines[(4*room.y)+i+1][:10*room.x +1] + 
                                     "x"*9 +
                                     lines[(4*room.y)+i+1][10*(room.x +1):])
        out = '\n'.join(lines)
        return out

                


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
        for i in range(len(self.base_grid)):
            for j in range(len(self.base_grid[i])):
                base_drawing = self.draw_room(self.base_grid[i][j], 
                                              base_drawing)

        print(base_drawing)

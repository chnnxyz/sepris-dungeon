from typing import List
from src.rooms.room import Room

class Grid:
    def __init__(self, rooms = List[Room]) -> None:
        # Initialize empty grid
        self.base_grid = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

        # Fill rooms

        for room in rooms:
            # Control for cases where x or y may get repeated
            if self.base_grid[room.x, room.y] is not None:
                self.base_grid[room.x,room.y] = room
            else:
                for row in self.base_grid:
                    try:
                        emptycol = self.base_grid[row].index(None)
                        self.base_grid[row,emptycol] = room
                    except:
                        continue

    def _check_colission(self):
        pass
    
    def shift_grid(self, direction:str):
        pass

    def move_room(self, direction:str, x:int, y:int):
        pass

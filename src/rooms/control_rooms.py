from src.rooms.room import Room
from src.dungeon.grid import Grid
from typing import List, Tuple

#TODO: add gravity methods
class GravityRoom(Room):
    
    def apply_gravity(self,direction:str,grid:Grid):
        grid.shift_grid(direction)

class PanelRoom(Room):

    def use_joystick(self,direction:str,grid:Grid,x:int,y:int):
        grid.move_room(direction,x,y)
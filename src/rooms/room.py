import random 
from typing import Tuple, List

class Room:
    '''
    A standard room, can contain up to four locked or unlocked doors
    The doors are initialized with a boolean saying if the door exists
    and a key name in case it is locked.
    '''
    def __init__(self,
                 room_name:str,
                 x:int,
                 y:int,
                 west_door:Tuple[bool, str] = None,
                 east_door:Tuple[bool, str] = None,
                 north_door:Tuple[bool, str] = None,
                 south_door:Tuple[bool, str] = None,
                 items:List[str] = [],
                 spawn_chance:float = 0,
                 ) -> None:
        '''
        Initializes a room with a user provided layout

        Arguments
        ----------
        - room_name [str]: Room identifier
        - <direction>_door [Tuple(bool,str)]: Wether a door exists and wether
                                              it is locked
        - items List[str]: Items contained in the room, mostly for dm assistance
        - spawn_chance [float]: chance of spawning enemies when entering (0-1)
        - x: x position
        - y: y position
        '''
        if (spawn_chance < 0 
            or spawn_chance > 1 
            or not isinstance(spawn_chance, (int,float))):

            raise ValueError('Spawn chance must be numeric between 0 and 1')

        self.room_name = room_name
        self.doors = {
            'north':north_door,
            'south':south_door,
            'east':east_door,
            'west':west_door
        }

        for key in self.doors.keys():
            # Account for potential Nones in doors
            if self.doors[key] is None:
                self.doors[key] = (False, None)

        self.items = items
        self.x = x
        self.y = y
        self.spawn_chance = spawn_chance
        self.party = False # Is the party in the room

    def _spawn(self):
        '''
        Helper to spawn random monsters
        '''
        rdm = random.random()
        if rdm <= self.spawn_chance:
            print('Enemies Spawned')

    def exit(self):
        '''
        Party exits the room
        '''

        self.party = False
    
    def enter(self) -> bool:
        '''
        Enter the room
        '''

        self.party = True
        self._spawn()

    def update_position(self,x:int,y:int) -> None:
        self.x = x
        self.y = y 
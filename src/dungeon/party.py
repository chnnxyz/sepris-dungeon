
class Party:
    def __init__(self,x:int, y:int) -> None:
        '''
        Instantiates a Party class in some position of the grid
        '''
        if x<0 or x>2 or y<0 or y>2:
            raise ValueError('x and y should be between 0 and 2')

        self.x = x
        self.y = y

    def move(self, x:int=0, y:int=0):
        '''
        Moves the grid position of the party
        '''
        if x !=0 and y!=0:
            raise ValueError('Party cannot move diagonally through the dungeon')
       
        if self.x + x >2 or self.x + x < 0:
            print('Cant move further on x')
            pass
        else:
            self.x += x
        
        if self.y + y >2 or self.y + y < 0:
            print('Cant move further on y')
            pass
        else:
            self.y += y 

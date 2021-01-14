'''
A text adventure game where a player can move between Rooms.

Classes:
--------

Room: A location within the game that has a description and exits to other
      Rooms

Game: The main game class.  A player can take actions within a game 

'''

class Room:
    def __init__(self, name):
        self.name = name
        self.description = ""
        self.exits = {}

    def __repr__(self):
        '''
        String representation of the class 
        '''
        desc = f"Room(name='{self.name}'"
        desc += f", description='{self.description[:20]}'"
        desc += f', n_exits={len(self.exits)})'
        return desc
                

    def add_exit(self, room, direction):
        '''
        Add an exit to the room

        Params:
        ------
        room: Room
            a Room object to link 

        direction: str
            The str command to access the room
        '''
        self.exits[direction] = room

    def exit(self, direction):
        '''
        Exit the room in the specified direction

        Params:
        ------
        direction: str
            A command string representing the direction.
        '''
        if direction in self.exits:
            return self.exits[direction]
        else:
            raise ValueError()

       
class TextWorld:
    '''
    A TextWorld encapsulate the logic and Room objects that comprise the game.
    '''
    def __init__(self, name, rooms, start_index=0):
        '''
        Constructor method for World

        Parameters:
        ----------
        rooms: list
            A list of rooms in the world.

        start_index: int, optional (default=0)
            The index of the room where the player begins their adventure.

        '''
        self.name = name
        self.rooms = rooms
        self.current_room = self.rooms[start_index]
        self.legal_exits = ['n', 'e', 's', 'w']
        self.legal_commands =['look']
        self.n_actions = 0
        
        #true while the game is active.
        self.active = True

    
    def __repr__(self):
        '''
        String representation of the class 
        '''
        desc = f"TextWorld(name='{self.name}', "
        desc += f'n_rooms={len(self.rooms)}, '
        desc += f'legal_exits={self.legal_exits}, '
        desc += f'legal_commands={self.legal_commands},\n'
        desc += f'\tcurrent_room={self.current_room})'
        return desc 


    def take_action(self, command):
        '''
        Take an action in the TextWorld

        Parameters:
        -----------
        command: str
            A command to parse and execute as a game action

        Returns:
        --------
        str: a string message to display to the player.
        '''

        #no. of actions taken
        self.n_actions += 1

        #handle action to move room
        if command in self.legal_exits:
            msg = ''
            try:
                self.current_room = self.current_room.exit(command)
                msg = self.current_room.description
            except ValueError:
                msg = 'You cannot go that way.'
            finally:
                return msg

        #split into array
        parsed_command = command.split()

        if parsed_command[0] in self.legal_commands:
            #handle command
            if parsed_command[0] == 'look':
                return self.current_room.description
        
        else:
            #handle command error
            return f"I don't know how to {command}"


        

        
if __name__ == '__main__':


    #create rooms
    #start fo the game = cliff edge
    origin = Room("origin")
    origin.description = 'You are stood on the edge of cliff. To the south' + \
                        ', east and west are steep drops to the sea below.' + \
                        ' A path to the north leads to a small beach.'
    beach = Room("beach")
    beach.description = 'A sandy beach by the sea.  To the south you can'+ \
                        ' see a high cliff edge. To the east you can enter' +\
                            ' the ocean.'

    ocean = Room("ocean")
    ocean.description = 'You are swimming in the deep blue ocean. The sea' + \
                            'is warm today. The shore is to the west.'

    origin.add_exit(beach, 'n')
    beach.add_exit(origin, 's')
    beach.add_exit(ocean, 'e')
    ocean.add_exit(beach, 'w')

    rooms = [origin, beach, ocean]

    game = Game(Player("player1"), rooms)

    #play the game

    opening = 'Welcome to your first OO text adventure!  Its not very exiting!'
    print('********************************************')
    print(opening, end='\n\n')

    print(game.current_room.description)

    while True:
        user_input = input("\nWhat do you want to do? >>> ")
        response = game.action(user_input)    
        print(response)
        





    

    


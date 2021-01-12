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


class Player:
    def __init__(self, name):
        self.name = name

        
class Game:
    def __init__(self, player, rooms, start_index=0):
        '''
        Parameters:
        ----------
        player: Player
            The player of the game is an instance of the player class.

        rooms: list
            A list of rooms in the game.

        start_index: int, optional (default=0)
            The index of the room where the player begins their adventure.

        '''
        self.player = player
        self.rooms = rooms
        self.current_room = self.rooms[start_index]
        self.legal_exits = ['n', 'e', 's', 'w']
        self.legal_commands =['look']
        self.moves = 0


    def action(self, command):
        '''
        Take an action in the game

        Parameters:
        -----------
        command: str
            A command to parse and execute as a game action

        Returns:
        --------
        str: a string message to display to the player.
        '''
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
        





    

    


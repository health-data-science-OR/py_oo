
class GameItem:
    def __init__(self, short_desc, long_desc):
        self.short_desc = short_desc
        self.long_desc = long_desc


class Room:
    def __init__(self, name, items):
        self.name = name
        self.items = items
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
        if direction in self.rooms:
            return self.rooms[direction]
        else:
            raise ValueError()


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        
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
        self.legal_commands =['look', 'get', 'inv', 'ex']
        self.moves = 0

    def action(self, command):

        #handle action to move room
        if command in self.legal_exits:
            try:
                self.current_room = self.current_room.exit(command)
                msg = self.current_room.long_desc
            except ValueError:
                msg = 'You cannot go that way.'
            finally:
                return msg

        #split into array
        parsed_command = command.split()

        if parsed_command[0] in self.legal_commands:
            #handle command
            if parsed_command[0] == 'look':
                return room.long_desc
            elif parsed_command[0] == 'ex'
                return player.inventory[parsed_command[1]].long_desc

        
        else:
            #handle command error
            return f'I don't know how to {command}'

            
    def parse_command(self, command):
        parsed = command.split()
        

        
if __name__ == '__main__':
    pass

        





    

    


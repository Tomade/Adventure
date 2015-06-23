__author__ = 'shade'

import cmd, textwrap
from adventure import Adventure

class GameCmd(cmd.Cmd):
    prompt = '\nWhat would you like to do? > '

    def default(self, arg):
        """The default action to take when the action is not understood."""
        print('I do not understand that command. Type "help" for a list of commands.')

    def do_quit(self, arg):
        """Quit the game."""
        return True

    def do_go(self, arg):
        print(maze.go(arg))

    def do_look(self, arg):
        """Check out the place"""
        print("You look at the {what} - Weird stuff!".format(what = arg))

if __name__ == "__main__":
    maze = Adventure("labyrinth.json")
    print(maze.describe_location())
    game = GameCmd()
    game.cmdloop()


__author__ = 'shade'

import cmd
from textwrap import fill
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
        print(fill(maze.go(arg)))

    def do_look_at(self, arg):
        """Examine something"""
        print(fill(maze.look_at(arg)))

    def do_search(self, arg):
        print(fill(maze.search(arg)))


if __name__ == "__main__":
    maze = Adventure("labyrinth.json")
    print(maze.describe_location())
    game = GameCmd()
    game.cmdloop()


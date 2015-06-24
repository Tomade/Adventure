


from flask import Flask, request
app = Flask(__name__)

__author__ = 'shade'

import cmd, textwrap
from adventure import Adventure

class GameCmd(cmd.Cmd):
    prompt = '\nWhat would you like to do? > '

    def default(self, arg):
        """The default action to take when the action is not understood."""
        return 'I do not understand that command. Type "help" for a list of commands.'

    def do_quit(self, arg):
        """Quit the game."""
        return True

    def do_go(self, arg):
        return maze.go(arg)

    def do_look_at(self, arg):
        """Examine something"""
        return maze.look_at(arg)

maze = Adventure("labyrinth.json")
game = GameCmd()

@app.route('/')
def hello_world():
    return '<form action="action" method="get"><input name="input" type="text"></form>'

@app.route('/action')
def action():
    return game.onecmd(request.args.get("input"))

if __name__ == '__main__':
    app.run(debug=True)
